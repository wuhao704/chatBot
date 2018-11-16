# Copyright 2018 Wu Hao.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================

from django.shortcuts import render
from django.http import HttpResponse
from django_ajax.decorators import ajax
import os
from django.template.loader import get_template
import re
from django.http import HttpResponse, HttpResponseRedirect
from django.http import StreamingHttpResponse
import sys
import socket  
import json


# your views here.
def index(request):
    print('before request')
    if request.POST:
        print('get request')

        host = '127.0.0.1'
        port = 12345
        address = (host, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        s.connect(address)  

        question = request.POST['inputText']
        question = question.encode()

        s.send(bytes(question))
        print('send question')
        answer=s.recv(512)
        answer=answer.decode()
        print('get answer')
        s.close()

        return HttpResponse(answer)

    else:
        template = get_template('chatchat/robot.html')
        html = template.render(locals())
        return HttpResponse(html)

