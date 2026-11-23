#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AiPayTemplateData import AiPayTemplateData


class AiPayConsultTemplate(object):

    def __init__(self):
        self._tpl = None
        self._tpl_id = None

    @property
    def tpl(self):
        return self._tpl

    @tpl.setter
    def tpl(self, value):
        if isinstance(value, AiPayTemplateData):
            self._tpl = value
        else:
            self._tpl = AiPayTemplateData.from_alipay_dict(value)
    @property
    def tpl_id(self):
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, value):
        self._tpl_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.tpl:
            if hasattr(self.tpl, 'to_alipay_dict'):
                params['tpl'] = self.tpl.to_alipay_dict()
            else:
                params['tpl'] = self.tpl
        if self.tpl_id:
            if hasattr(self.tpl_id, 'to_alipay_dict'):
                params['tpl_id'] = self.tpl_id.to_alipay_dict()
            else:
                params['tpl_id'] = self.tpl_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AiPayConsultTemplate()
        if 'tpl' in d:
            o.tpl = d['tpl']
        if 'tpl_id' in d:
            o.tpl_id = d['tpl_id']
        return o


