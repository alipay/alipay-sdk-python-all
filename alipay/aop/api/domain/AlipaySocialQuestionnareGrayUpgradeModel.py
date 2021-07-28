#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialQuestionnareGrayUpgradeModel(object):

    def __init__(self):
        self._ext_info = None
        self._gray_percent = None
        self._qstn_id = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gray_percent(self):
        return self._gray_percent

    @gray_percent.setter
    def gray_percent(self, value):
        self._gray_percent = value
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
        if self.gray_percent:
            if hasattr(self.gray_percent, 'to_alipay_dict'):
                params['gray_percent'] = self.gray_percent.to_alipay_dict()
            else:
                params['gray_percent'] = self.gray_percent
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
        o = AlipaySocialQuestionnareGrayUpgradeModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gray_percent' in d:
            o.gray_percent = d['gray_percent']
        if 'qstn_id' in d:
            o.qstn_id = d['qstn_id']
        return o


