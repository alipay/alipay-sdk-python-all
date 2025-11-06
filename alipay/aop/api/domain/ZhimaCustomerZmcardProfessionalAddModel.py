#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ZmCardPictureInfo import ZmCardPictureInfo
from alipay.aop.api.domain.ZmCarOwnerEvaluateInfo import ZmCarOwnerEvaluateInfo
from alipay.aop.api.domain.ZmCarOwnerOrderInfo import ZmCarOwnerOrderInfo
from alipay.aop.api.domain.ZmCardPictureInfo import ZmCardPictureInfo


class ZhimaCustomerZmcardProfessionalAddModel(object):

    def __init__(self):
        self._cert_name = None
        self._cert_no = None
        self._certification_list = None
        self._conn_key = None
        self._evaluate_info = None
        self._open_id = None
        self._order_info = None
        self._picture_list = None
        self._role_type = None
        self._specialties = None
        self._user_id = None
        self._working_years_in_field = None

    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def certification_list(self):
        return self._certification_list

    @certification_list.setter
    def certification_list(self, value):
        if isinstance(value, list):
            self._certification_list = list()
            for i in value:
                if isinstance(i, ZmCardPictureInfo):
                    self._certification_list.append(i)
                else:
                    self._certification_list.append(ZmCardPictureInfo.from_alipay_dict(i))
    @property
    def conn_key(self):
        return self._conn_key

    @conn_key.setter
    def conn_key(self, value):
        self._conn_key = value
    @property
    def evaluate_info(self):
        return self._evaluate_info

    @evaluate_info.setter
    def evaluate_info(self, value):
        if isinstance(value, ZmCarOwnerEvaluateInfo):
            self._evaluate_info = value
        else:
            self._evaluate_info = ZmCarOwnerEvaluateInfo.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_info(self):
        return self._order_info

    @order_info.setter
    def order_info(self, value):
        if isinstance(value, ZmCarOwnerOrderInfo):
            self._order_info = value
        else:
            self._order_info = ZmCarOwnerOrderInfo.from_alipay_dict(value)
    @property
    def picture_list(self):
        return self._picture_list

    @picture_list.setter
    def picture_list(self, value):
        if isinstance(value, list):
            self._picture_list = list()
            for i in value:
                if isinstance(i, ZmCardPictureInfo):
                    self._picture_list.append(i)
                else:
                    self._picture_list.append(ZmCardPictureInfo.from_alipay_dict(i))
    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value
    @property
    def specialties(self):
        return self._specialties

    @specialties.setter
    def specialties(self, value):
        if isinstance(value, list):
            self._specialties = list()
            for i in value:
                self._specialties.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def working_years_in_field(self):
        return self._working_years_in_field

    @working_years_in_field.setter
    def working_years_in_field(self, value):
        self._working_years_in_field = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.certification_list:
            if isinstance(self.certification_list, list):
                for i in range(0, len(self.certification_list)):
                    element = self.certification_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.certification_list[i] = element.to_alipay_dict()
            if hasattr(self.certification_list, 'to_alipay_dict'):
                params['certification_list'] = self.certification_list.to_alipay_dict()
            else:
                params['certification_list'] = self.certification_list
        if self.conn_key:
            if hasattr(self.conn_key, 'to_alipay_dict'):
                params['conn_key'] = self.conn_key.to_alipay_dict()
            else:
                params['conn_key'] = self.conn_key
        if self.evaluate_info:
            if hasattr(self.evaluate_info, 'to_alipay_dict'):
                params['evaluate_info'] = self.evaluate_info.to_alipay_dict()
            else:
                params['evaluate_info'] = self.evaluate_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_info:
            if hasattr(self.order_info, 'to_alipay_dict'):
                params['order_info'] = self.order_info.to_alipay_dict()
            else:
                params['order_info'] = self.order_info
        if self.picture_list:
            if isinstance(self.picture_list, list):
                for i in range(0, len(self.picture_list)):
                    element = self.picture_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.picture_list[i] = element.to_alipay_dict()
            if hasattr(self.picture_list, 'to_alipay_dict'):
                params['picture_list'] = self.picture_list.to_alipay_dict()
            else:
                params['picture_list'] = self.picture_list
        if self.role_type:
            if hasattr(self.role_type, 'to_alipay_dict'):
                params['role_type'] = self.role_type.to_alipay_dict()
            else:
                params['role_type'] = self.role_type
        if self.specialties:
            if isinstance(self.specialties, list):
                for i in range(0, len(self.specialties)):
                    element = self.specialties[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.specialties[i] = element.to_alipay_dict()
            if hasattr(self.specialties, 'to_alipay_dict'):
                params['specialties'] = self.specialties.to_alipay_dict()
            else:
                params['specialties'] = self.specialties
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.working_years_in_field:
            if hasattr(self.working_years_in_field, 'to_alipay_dict'):
                params['working_years_in_field'] = self.working_years_in_field.to_alipay_dict()
            else:
                params['working_years_in_field'] = self.working_years_in_field
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerZmcardProfessionalAddModel()
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'certification_list' in d:
            o.certification_list = d['certification_list']
        if 'conn_key' in d:
            o.conn_key = d['conn_key']
        if 'evaluate_info' in d:
            o.evaluate_info = d['evaluate_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_info' in d:
            o.order_info = d['order_info']
        if 'picture_list' in d:
            o.picture_list = d['picture_list']
        if 'role_type' in d:
            o.role_type = d['role_type']
        if 'specialties' in d:
            o.specialties = d['specialties']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'working_years_in_field' in d:
            o.working_years_in_field = d['working_years_in_field']
        return o


