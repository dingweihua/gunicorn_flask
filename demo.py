#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: 布丁(dingweihuaic@126.com)
#
# Created: 2018/3/14 上午11:01

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1 style=\'color: blue\'>Hello World!</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
