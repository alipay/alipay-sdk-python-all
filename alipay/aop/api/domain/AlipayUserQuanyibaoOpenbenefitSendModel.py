#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QYBMapInfo import QYBMapInfo


class AlipayUserQuanyibaoOpenbenefitSendModel(object):

    def __init__(self):
        self._alipay_login_id = None
        self._alipay_user_id = None
        self._benefit_id = None
        self._ext_info = None
        self._memo = None
        self._third_biz_no = None

    @property
    def alipay_login_id(self):
        return self._alipay_login_id

    @alipay_login_id.setter
    def alipay_login_id(self, value):
        self._alipay_login_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, QYBMapInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(QYBMapInfo.from_alipay_dict(i))
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def third_biz_no(self):
        return self._third_biz_no

    @third_biz_no.setter
    def third_biz_no(self, value):
        self._third_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_login_id:
            if hasattr(self.alipay_login_id, 'to_alipay_dict'):
                params['alipay_login_id'] = self.alipay_login_id.to_alipay_dict()
            else:
                params['alipay_login_id'] = self.alipay_login_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.third_biz_no:
            if hasattr(self.third_biz_no, 'to_alipay_dict'):
                params['third_biz_no'] = self.third_biz_no.to_alipay_dict()
            else:
                params['third_biz_no'] = self.third_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserQuanyibaoOpenbenefitSendModel()
        if 'alipay_login_id' in d:
            o.alipay_login_id = d['alipay_login_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'memo' in d:
            o.memo = d['memo']
        if 'third_biz_no' in d:
            o.third_biz_no = d['third_biz_no']
        return o


