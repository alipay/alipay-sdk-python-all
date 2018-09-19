#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HoloGraphicContactInfo import HoloGraphicContactInfo


class AlipayDataDataserviceHolographicFactorQueryModel(object):

    def __init__(self):
        self._biz_id = None
        self._cert_no = None
        self._contact_info_list = None
        self._isv_feature = None
        self._mobile = None
        self._user_name = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def contact_info_list(self):
        return self._contact_info_list

    @contact_info_list.setter
    def contact_info_list(self, value):
        if isinstance(value, list):
            self._contact_info_list = list()
            for i in value:
                if isinstance(i, HoloGraphicContactInfo):
                    self._contact_info_list.append(i)
                else:
                    self._contact_info_list.append(HoloGraphicContactInfo.from_alipay_dict(i))
    @property
    def isv_feature(self):
        return self._isv_feature

    @isv_feature.setter
    def isv_feature(self, value):
        self._isv_feature = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.contact_info_list:
            if isinstance(self.contact_info_list, list):
                for i in range(0, len(self.contact_info_list)):
                    element = self.contact_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contact_info_list[i] = element.to_alipay_dict()
            if hasattr(self.contact_info_list, 'to_alipay_dict'):
                params['contact_info_list'] = self.contact_info_list.to_alipay_dict()
            else:
                params['contact_info_list'] = self.contact_info_list
        if self.isv_feature:
            if hasattr(self.isv_feature, 'to_alipay_dict'):
                params['isv_feature'] = self.isv_feature.to_alipay_dict()
            else:
                params['isv_feature'] = self.isv_feature
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceHolographicFactorQueryModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'contact_info_list' in d:
            o.contact_info_list = d['contact_info_list']
        if 'isv_feature' in d:
            o.isv_feature = d['isv_feature']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


