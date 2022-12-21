#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SpeechRecordDetail import SpeechRecordDetail


class AlipayMerchantIndirectIotdataBatchcreateModel(object):

    def __init__(self):
        self._speech_record_list = None

    @property
    def speech_record_list(self):
        return self._speech_record_list

    @speech_record_list.setter
    def speech_record_list(self, value):
        if isinstance(value, list):
            self._speech_record_list = list()
            for i in value:
                if isinstance(i, SpeechRecordDetail):
                    self._speech_record_list.append(i)
                else:
                    self._speech_record_list.append(SpeechRecordDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.speech_record_list:
            if isinstance(self.speech_record_list, list):
                for i in range(0, len(self.speech_record_list)):
                    element = self.speech_record_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.speech_record_list[i] = element.to_alipay_dict()
            if hasattr(self.speech_record_list, 'to_alipay_dict'):
                params['speech_record_list'] = self.speech_record_list.to_alipay_dict()
            else:
                params['speech_record_list'] = self.speech_record_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantIndirectIotdataBatchcreateModel()
        if 'speech_record_list' in d:
            o.speech_record_list = d['speech_record_list']
        return o


