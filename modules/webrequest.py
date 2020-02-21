
from urllib import request
from random import randint, shuffle

__slots__ = ['atErr', 'atBody', 'atHeader', 'atCodeFull', 'atCode', 'atTitle']


class WebRequest:

    def __setUserAgentRandom(self):
        ''' CREATE UA_STRING RANDOMIC
        Ref: https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/User-Agent
        '''
        browser = ['Firefox', 'Safari', 'Opera',
                   'Internet Explorer',  'Chrome']
        os = ['Windows', 'FreeBSD', 'Redhat',
              'Linux', 'Ubuntu', 'Fedora']
        locais = ['cs-CZ', 'en-US', 'sk-SK', 'pt-BR',
                  'pt', 'ms', 'mt_MT']

        elements_user_agent = [browser, os, locais]
        for element_rand in elements_user_agent:
            shuffle(element_rand)

        awk_int, browser_int = randint(1, 537), randint(1, 537)
        user_agent_str = f'{browser[0]}/5.0 (X11; {os[0]} x86_64) AppleWebKit/{awk_int}.36 (KHTML, like Gecko) {browser[0]}/51.0.2704.103 {browser[0]}/{browser_int}.36'

        return user_agent_str

    def findTitle(self):
        ''' GREP TAG TITLE FROM RESULT REQUEST
        Ref: https://stackoverflow.com/a/33272707
        '''
        title = str(self.atBody).split('<title>')[1].split('</title>')[0]
        return title

    def sendRequest(self, url_request):
        try:
            header_set = {'User-Agent': self.__setUserAgentRandom()}
            connection = request.Request(url_request, headers=header_set)
            response = request.urlopen(connection)

            self.atBody = response.read()
            self.atHeader = response.headers
            self.atCodeFull = response.code
            self.atCode = int(''.join(filter(str.isdigit, str(response.code))))
            self.atTitle = self.findTitle()

            return {'response': self.atBody, 'header': self.atHeader, 'code': self.atCodeFull,
                    'url_request': response.url, 'code_clear': self.atCode, 'title': self.atTitle}
        except Exception as e:
            self.atErr = str(e)
