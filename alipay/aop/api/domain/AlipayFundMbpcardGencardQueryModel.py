#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundMbpcardGencardQueryModel(object):

    def __init__(self):
        self._buyer_user_id = None
        self._gen_card_no = None
        self._open_id = None
        self._out_request_no = None

    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def gen_card_no(self):
        return self._gen_card_no

    @gen_card_no.setter
    def gen_card_no(self, value):
        self._gen_card_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_user_id:
            if hasattr(self.buyer_user_id, 'to_alipay_dict'):
                params['buyer_user_id'] = self.buyer_user_id.to_alipay_dict()
            else:
                params['buyer_user_id'] = self.buyer_user_id
        if self.gen_card_no:
            if hasattr(self.gen_card_no, 'to_alipay_dict'):
                params['gen_card_no'] = self.gen_card_no.to_alipay_dict()
            else:
                params['gen_card_no'] = self.gen_card_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        if 'buyer_user_id' in d:
            o.buyer_user_id = d['buyer_user_id']
        if 'gen_card_no' in d:
            o.gen_card_no = d['gen_card_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        return o


