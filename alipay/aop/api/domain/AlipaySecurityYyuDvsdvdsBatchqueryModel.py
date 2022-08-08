#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PageTemplateParamInfoDTO import PageTemplateParamInfoDTO


class AlipaySecurityYyuDvsdvdsBatchqueryModel(object):

    def __init__(self):
        self._asd = None
        self._asdasda = None
        self._asdf = None
        self._sadf = None
        self._yuyu = None

    @property
    def asd(self):
        return self._asd

    @asd.setter
    def asd(self, value):
        if isinstance(value, PageTemplateParamInfoDTO):
            self._asd = value
        else:
            self._asd = PageTemplateParamInfoDTO.from_alipay_dict(value)
    @property
    def asdasda(self):
        return self._asdasda

    @asdasda.setter
    def asdasda(self, value):
        self._asdasda = value
    @property
    def asdf(self):
        return self._asdf

    @asdf.setter
    def asdf(self, value):
        self._asdf = value
    @property
    def sadf(self):
        return self._sadf

    @sadf.setter
    def sadf(self, value):
        self._sadf = value
    @property
    def yuyu(self):
        return self._yuyu

    @yuyu.setter
    def yuyu(self, value):
        self._yuyu = value


    def to_alipay_dict(self):
        params = dict()
        if self.asd:
            if hasattr(self.asd, 'to_alipay_dict'):
                params['asd'] = self.asd.to_alipay_dict()
            else:
                params['asd'] = self.asd
        if self.asdasda:
            if hasattr(self.asdasda, 'to_alipay_dict'):
                params['asdasda'] = self.asdasda.to_alipay_dict()
            else:
                params['asdasda'] = self.asdasda
        if self.asdf:
            if hasattr(self.asdf, 'to_alipay_dict'):
                params['asdf'] = self.asdf.to_alipay_dict()
            else:
                params['asdf'] = self.asdf
        if self.sadf:
            if hasattr(self.sadf, 'to_alipay_dict'):
                params['sadf'] = self.sadf.to_alipay_dict()
            else:
                params['sadf'] = self.sadf
        if self.yuyu:
            if hasattr(self.yuyu, 'to_alipay_dict'):
                params['yuyu'] = self.yuyu.to_alipay_dict()
            else:
                params['yuyu'] = self.yuyu
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityYyuDvsdvdsBatchqueryModel()
        if 'asd' in d:
            o.asd = d['asd']
        if 'asdasda' in d:
            o.asdasda = d['asdasda']
        if 'asdf' in d:
            o.asdf = d['asdf']
        if 'sadf' in d:
            o.sadf = d['sadf']
        if 'yuyu' in d:
            o.yuyu = d['yuyu']
        return o


