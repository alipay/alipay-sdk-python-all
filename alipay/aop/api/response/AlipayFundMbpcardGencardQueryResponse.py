#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundMbpcardGencardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundMbpcardGencardQueryResponse, self).__init__()
        self._file_path_list = None
        self._gen_card_no = None
        self._result_code = None
        self._result_msg = None
        self._status = None

    @property
    def file_path_list(self):
        return self._file_path_list

    @file_path_list.setter
    def file_path_list(self, value):
        if isinstance(value, list):
            self._file_path_list = list()
            for i in value:
                self._file_path_list.append(i)
    @property
    def gen_card_no(self):
        return self._gen_card_no

    @gen_card_no.setter
    def gen_card_no(self, value):
        self._gen_card_no = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundMbpcardGencardQueryResponse, self).parse_response_content(response_content)
        if 'file_path_list' in response:
            self.file_path_list = response['file_path_list']
        if 'gen_card_no' in response:
            self.gen_card_no = response['gen_card_no']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
        if 'status' in response:
            self.status = response['status']
