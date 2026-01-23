#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HmAppointInfo import HmAppointInfo


class AlipayCommerceMedicalHmEquityorderstatusSyncModel(object):

    def __init__(self):
        self._appoint_info_list = None
        self._hm_uid = None
        self._order_id = None
        self._order_status = None

    @property
    def appoint_info_list(self):
        return self._appoint_info_list

    @appoint_info_list.setter
    def appoint_info_list(self, value):
        if isinstance(value, list):
            self._appoint_info_list = list()
            for i in value:
                if isinstance(i, HmAppointInfo):
                    self._appoint_info_list.append(i)
                else:
                    self._appoint_info_list.append(HmAppointInfo.from_alipay_dict(i))
    @property
    def hm_uid(self):
        return self._hm_uid

    @hm_uid.setter
    def hm_uid(self, value):
        self._hm_uid = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.appoint_info_list:
            if isinstance(self.appoint_info_list, list):
                for i in range(0, len(self.appoint_info_list)):
                    element = self.appoint_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.appoint_info_list[i] = element.to_alipay_dict()
            if hasattr(self.appoint_info_list, 'to_alipay_dict'):
                params['appoint_info_list'] = self.appoint_info_list.to_alipay_dict()
            else:
                params['appoint_info_list'] = self.appoint_info_list
        if self.hm_uid:
            if hasattr(self.hm_uid, 'to_alipay_dict'):
                params['hm_uid'] = self.hm_uid.to_alipay_dict()
            else:
                params['hm_uid'] = self.hm_uid
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHmEquityorderstatusSyncModel()
        if 'appoint_info_list' in d:
            o.appoint_info_list = d['appoint_info_list']
        if 'hm_uid' in d:
            o.hm_uid = d['hm_uid']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        return o


