#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromiseDetail import PromiseDetail
from alipay.aop.api.domain.JinyouTestFive import JinyouTestFive


class AlipaySecurityProdSssQueryModel(object):

    def __init__(self):
        self._aaa = None
        self._aaa_open_id = None
        self._bbb = None
        self._tesst = None
        self._xxx = None

    @property
    def aaa(self):
        return self._aaa

    @aaa.setter
    def aaa(self, value):
        self._aaa = value
    @property
    def aaa_open_id(self):
        return self._aaa_open_id

    @aaa_open_id.setter
    def aaa_open_id(self, value):
        self._aaa_open_id = value
    @property
    def bbb(self):
        return self._bbb

    @bbb.setter
    def bbb(self, value):
        self._bbb = value
    @property
    def tesst(self):
        return self._tesst

    @tesst.setter
    def tesst(self, value):
        if isinstance(value, list):
            self._tesst = list()
            for i in value:
                if isinstance(i, PromiseDetail):
                    self._tesst.append(i)
                else:
                    self._tesst.append(PromiseDetail.from_alipay_dict(i))
    @property
    def xxx(self):
        return self._xxx

    @xxx.setter
    def xxx(self, value):
        if isinstance(value, JinyouTestFive):
            self._xxx = value
        else:
            self._xxx = JinyouTestFive.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.aaa:
            if hasattr(self.aaa, 'to_alipay_dict'):
                params['aaa'] = self.aaa.to_alipay_dict()
            else:
                params['aaa'] = self.aaa
        if self.aaa_open_id:
            if hasattr(self.aaa_open_id, 'to_alipay_dict'):
                params['aaa_open_id'] = self.aaa_open_id.to_alipay_dict()
            else:
                params['aaa_open_id'] = self.aaa_open_id
        if self.bbb:
            if hasattr(self.bbb, 'to_alipay_dict'):
                params['bbb'] = self.bbb.to_alipay_dict()
            else:
                params['bbb'] = self.bbb
        if self.tesst:
            if isinstance(self.tesst, list):
                for i in range(0, len(self.tesst)):
                    element = self.tesst[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tesst[i] = element.to_alipay_dict()
            if hasattr(self.tesst, 'to_alipay_dict'):
                params['tesst'] = self.tesst.to_alipay_dict()
            else:
                params['tesst'] = self.tesst
        if self.xxx:
            if hasattr(self.xxx, 'to_alipay_dict'):
                params['xxx'] = self.xxx.to_alipay_dict()
            else:
                params['xxx'] = self.xxx
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdSssQueryModel()
        if 'aaa' in d:
            o.aaa = d['aaa']
        if 'aaa_open_id' in d:
            o.aaa_open_id = d['aaa_open_id']
        if 'bbb' in d:
            o.bbb = d['bbb']
        if 'tesst' in d:
            o.tesst = d['tesst']
        if 'xxx' in d:
            o.xxx = d['xxx']
        return o


