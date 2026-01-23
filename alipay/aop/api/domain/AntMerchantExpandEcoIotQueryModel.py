#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandEcoIotQueryModel(object):

    def __init__(self):
        self._out_biz_nos = None
        self._page_num = None
        self._sn = None

    @property
    def out_biz_nos(self):
        return self._out_biz_nos

    @out_biz_nos.setter
    def out_biz_nos(self, value):
        if isinstance(value, list):
            self._out_biz_nos = list()
            for i in value:
                self._out_biz_nos.append(i)
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        if isinstance(value, list):
            self._sn = list()
            for i in value:
                self._sn.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_nos:
            if isinstance(self.out_biz_nos, list):
                for i in range(0, len(self.out_biz_nos)):
                    element = self.out_biz_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_biz_nos[i] = element.to_alipay_dict()
            if hasattr(self.out_biz_nos, 'to_alipay_dict'):
                params['out_biz_nos'] = self.out_biz_nos.to_alipay_dict()
            else:
                params['out_biz_nos'] = self.out_biz_nos
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.sn:
            if isinstance(self.sn, list):
                for i in range(0, len(self.sn)):
                    element = self.sn[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sn[i] = element.to_alipay_dict()
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandEcoIotQueryModel()
        if 'out_biz_nos' in d:
            o.out_biz_nos = d['out_biz_nos']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'sn' in d:
            o.sn = d['sn']
        return o


