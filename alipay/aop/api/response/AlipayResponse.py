#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


class AlipayResponse(object):

    def __init__(self):
        self.code = None
        self.msg = None
        self.sub_code = None
        self.sub_msg = None
        self.body = None

    def is_success(self):
        return not self.sub_code

    def parse_response_content(self, response_content):
        response = json.loads(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'msg' in response:
            self.msg = response['msg']
        if 'sub_code' in response:
            self.sub_code = response['sub_code']
        if 'sub_msg' in response:
            self.sub_msg = response['sub_msg']
        self.body = response_content
        return response

