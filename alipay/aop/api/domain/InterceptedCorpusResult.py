#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InterceptedCorpusResult(object):

    def __init__(self):
        self._msg = None
        self._out_corpus_id_list = None

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def out_corpus_id_list(self):
        return self._out_corpus_id_list

    @out_corpus_id_list.setter
    def out_corpus_id_list(self, value):
        if isinstance(value, list):
            self._out_corpus_id_list = list()
            for i in value:
                self._out_corpus_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.msg:
            if hasattr(self.msg, 'to_alipay_dict'):
                params['msg'] = self.msg.to_alipay_dict()
            else:
                params['msg'] = self.msg
        if self.out_corpus_id_list:
            if isinstance(self.out_corpus_id_list, list):
                for i in range(0, len(self.out_corpus_id_list)):
                    element = self.out_corpus_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_corpus_id_list[i] = element.to_alipay_dict()
            if hasattr(self.out_corpus_id_list, 'to_alipay_dict'):
                params['out_corpus_id_list'] = self.out_corpus_id_list.to_alipay_dict()
            else:
                params['out_corpus_id_list'] = self.out_corpus_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InterceptedCorpusResult()
        if 'msg' in d:
            o.msg = d['msg']
        if 'out_corpus_id_list' in d:
            o.out_corpus_id_list = d['out_corpus_id_list']
        return o


