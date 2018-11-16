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

import socket
import sys
# this path need to modify to your path
sys.path.append('/Users/wuhao/DjangoProjects/chatBot/chatchat/')
import os
import tensorflow as tf

from botpredictor import BotPredictor
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

corp_dir = os.path.join(PROJECT_ROOT, 'Data', 'Corpus')
knbs_dir = os.path.join(PROJECT_ROOT, 'Data', 'KnowledgeBase')
res_dir = os.path.join(PROJECT_ROOT, 'Data', 'Result')

host = '127.0.0.1'
port = 12345
address = (host, port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
s.bind(address)
s.listen(5)
with tf.Session() as sess:
    predictor = BotPredictor(sess, corpus_dir=corp_dir, knbase_dir=knbs_dir,
                             result_dir=res_dir, result_file='basic')
    session_id = predictor.session_data.add_session()

    while True:
        ss, addr = s.accept() 
        print ('got connected from'+str(addr)) 

        try:
 
            question = ss.recv(512)
            question = question.decode('utf-8')
            print('get question')


            answer = predictor.predict(session_id, question)
            answer = answer.encode()
            sys.stdout.flush()
            ss.send(bytes(answer))
            print("send answer")

        finally:
            ss.close()

