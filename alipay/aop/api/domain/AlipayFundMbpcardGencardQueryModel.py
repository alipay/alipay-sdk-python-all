#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundMbpcardGencardQueryModel(object):

    def __init__(self):
        self._gen_card_no = None
        self._out_request_no = None

    @property
    def gen_card_no(self):
        return self._gen_card_no

    @gen_card_no.setter
    def gen_card_no(self, value):
        self._gen_card_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.gen_card_no:
            if hasattr(self.gen_card_no, 'to_alipay_dict'):
                params['gen_card_no'] = self.gen_card_no.to_alipay_dict()
            else:
                params['gen_card_no'] = self.gen_card_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundMbpcardGencardQueryModel()
        if 'gen_card_no' in d:
            o.gen_card_no = d['gen_card_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        return o


