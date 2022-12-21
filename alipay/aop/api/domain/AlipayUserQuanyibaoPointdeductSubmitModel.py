#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QYBMapInfo import QYBMapInfo


class AlipayUserQuanyibaoPointdeductSubmitModel(object):

    def __init__(self):
        self._alipay_biz_no = None
        self._alipay_user_id = None
        self._deduct_status = None
        self._ext_info_list = None
        self._open_id = None
        self._third_biz_no = None
        self._third_user_id = None

    @property
    def alipay_biz_no(self):
        return self._alipay_biz_no

    @alipay_biz_no.setter
    def alipay_biz_no(self, value):
        self._alipay_biz_no = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def deduct_status(self):
        return self._deduct_status

    @deduct_status.setter
    def deduct_status(self, value):
        self._deduct_status = value
    @property
    def ext_info_list(self):
        return self._ext_info_list

    @ext_info_list.setter
    def ext_info_list(self, value):
        if isinstance(value, list):
            self._ext_info_list = list()
            for i in value:
                if isinstance(i, QYBMapInfo):
                    self._ext_info_list.append(i)
                else:
                    self._ext_info_list.append(QYBMapInfo.from_alipay_dict(i))
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def third_biz_no(self):
        return self._third_biz_no

    @third_biz_no.setter
    def third_biz_no(self, value):
        self._third_biz_no = value
    @property
    def third_user_id(self):
        return self._third_user_id

    @third_user_id.setter
    def third_user_id(self, value):
        self._third_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_biz_no:
            if hasattr(self.alipay_biz_no, 'to_alipay_dict'):
                params['alipay_biz_no'] = self.alipay_biz_no.to_alipay_dict()
            else:
                params['alipay_biz_no'] = self.alipay_biz_no
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.deduct_status:
            if hasattr(self.deduct_status, 'to_alipay_dict'):
                params['deduct_status'] = self.deduct_status.to_alipay_dict()
            else:
                params['deduct_status'] = self.deduct_status
        if self.ext_info_list:
            if isinstance(self.ext_info_list, list):
                for i in range(0, len(self.ext_info_list)):
                    element = self.ext_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info_list[i] = element.to_alipay_dict()
            if hasattr(self.ext_info_list, 'to_alipay_dict'):
                params['ext_info_list'] = self.ext_info_list.to_alipay_dict()
            else:
                params['ext_info_list'] = self.ext_info_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.third_biz_no:
            if hasattr(self.third_biz_no, 'to_alipay_dict'):
                params['third_biz_no'] = self.third_biz_no.to_alipay_dict()
            else:
                params['third_biz_no'] = self.third_biz_no
        if self.third_user_id:
            if hasattr(self.third_user_id, 'to_alipay_dict'):
                params['third_user_id'] = self.third_user_id.to_alipay_dict()
            else:
                params['third_user_id'] = self.third_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserQuanyibaoPointdeductSubmitModel()
        if 'alipay_biz_no' in d:
            o.alipay_biz_no = d['alipay_biz_no']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'deduct_status' in d:
            o.deduct_status = d['deduct_status']
        if 'ext_info_list' in d:
            o.ext_info_list = d['ext_info_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'third_biz_no' in d:
            o.third_biz_no = d['third_biz_no']
        if 'third_user_id' in d:
            o.third_user_id = d['third_user_id']
        return o


