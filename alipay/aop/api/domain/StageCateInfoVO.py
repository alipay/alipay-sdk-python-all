#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CateInfoVO import CateInfoVO


class StageCateInfoVO(object):

    def __init__(self):
        self._cate_infos = None
        self._code = None
        self._name = None

    @property
    def cate_infos(self):
        return self._cate_infos

    @cate_infos.setter
    def cate_infos(self, value):
        if isinstance(value, list):
            self._cate_infos = list()
            for i in value:
                if isinstance(i, CateInfoVO):
                    self._cate_infos.append(i)
                else:
                    self._cate_infos.append(CateInfoVO.from_alipay_dict(i))
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cate_infos:
            if isinstance(self.cate_infos, list):
                for i in range(0, len(self.cate_infos)):
                    element = self.cate_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cate_infos[i] = element.to_alipay_dict()
            if hasattr(self.cate_infos, 'to_alipay_dict'):
                params['cate_infos'] = self.cate_infos.to_alipay_dict()
            else:
                params['cate_infos'] = self.cate_infos
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StageCateInfoVO()
        if 'cate_infos' in d:
            o.cate_infos = d['cate_infos']
        if 'code' in d:
            o.code = d['code']
        if 'name' in d:
            o.name = d['name']
        return o


