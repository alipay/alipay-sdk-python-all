#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialQuestionnareTaskFinishModel(object):

    def __init__(self):
        self._ext_info = None
        self._qstn_id = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def qstn_id(self):
        return self._qstn_id

    @qstn_id.setter
    def qstn_id(self, value):
        self._qstn_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.qstn_id:
            if hasattr(self.qstn_id, 'to_alipay_dict'):
                params['qstn_id'] = self.qstn_id.to_alipay_dict()
            else:
                params['qstn_id'] = self.qstn_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialQuestionnareTaskFinishModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'qstn_id' in d:
            o.qstn_id = d['qstn_id']
        return o


