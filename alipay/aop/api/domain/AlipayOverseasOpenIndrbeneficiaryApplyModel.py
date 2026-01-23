#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndrAddress import IndrAddress
from alipay.aop.api.domain.IndrFileInfo import IndrFileInfo


class AlipayOverseasOpenIndrbeneficiaryApplyModel(object):

    def __init__(self):
        self._address = None
        self._beneficiary_abb_name = None
        self._beneficiary_local_name = None
        self._beneficiary_name = None
        self._beneficiary_sub_type = None
        self._beneficiary_type = None
        self._email = None
        self._file_list = None
        self._phone_number = None
        self._remark = None
        self._scene_type = None
        self._websites = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, IndrAddress):
            self._address = value
        else:
            self._address = IndrAddress.from_alipay_dict(value)
    @property
    def beneficiary_abb_name(self):
        return self._beneficiary_abb_name

    @beneficiary_abb_name.setter
    def beneficiary_abb_name(self, value):
        self._beneficiary_abb_name = value
    @property
    def beneficiary_local_name(self):
        return self._beneficiary_local_name

    @beneficiary_local_name.setter
    def beneficiary_local_name(self, value):
        self._beneficiary_local_name = value
    @property
    def beneficiary_name(self):
        return self._beneficiary_name

    @beneficiary_name.setter
    def beneficiary_name(self, value):
        self._beneficiary_name = value
    @property
    def beneficiary_sub_type(self):
        return self._beneficiary_sub_type

    @beneficiary_sub_type.setter
    def beneficiary_sub_type(self, value):
        self._beneficiary_sub_type = value
    @property
    def beneficiary_type(self):
        return self._beneficiary_type

    @beneficiary_type.setter
    def beneficiary_type(self, value):
        self._beneficiary_type = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def file_list(self):
        return self._file_list

    @file_list.setter
    def file_list(self, value):
        if isinstance(value, list):
            self._file_list = list()
            for i in value:
                if isinstance(i, IndrFileInfo):
                    self._file_list.append(i)
                else:
                    self._file_list.append(IndrFileInfo.from_alipay_dict(i))
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def websites(self):
        return self._websites

    @websites.setter
    def websites(self, value):
        self._websites = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.beneficiary_abb_name:
            if hasattr(self.beneficiary_abb_name, 'to_alipay_dict'):
                params['beneficiary_abb_name'] = self.beneficiary_abb_name.to_alipay_dict()
            else:
                params['beneficiary_abb_name'] = self.beneficiary_abb_name
        if self.beneficiary_local_name:
            if hasattr(self.beneficiary_local_name, 'to_alipay_dict'):
                params['beneficiary_local_name'] = self.beneficiary_local_name.to_alipay_dict()
            else:
                params['beneficiary_local_name'] = self.beneficiary_local_name
        if self.beneficiary_name:
            if hasattr(self.beneficiary_name, 'to_alipay_dict'):
                params['beneficiary_name'] = self.beneficiary_name.to_alipay_dict()
            else:
                params['beneficiary_name'] = self.beneficiary_name
        if self.beneficiary_sub_type:
            if hasattr(self.beneficiary_sub_type, 'to_alipay_dict'):
                params['beneficiary_sub_type'] = self.beneficiary_sub_type.to_alipay_dict()
            else:
                params['beneficiary_sub_type'] = self.beneficiary_sub_type
        if self.beneficiary_type:
            if hasattr(self.beneficiary_type, 'to_alipay_dict'):
                params['beneficiary_type'] = self.beneficiary_type.to_alipay_dict()
            else:
                params['beneficiary_type'] = self.beneficiary_type
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.file_list:
            if isinstance(self.file_list, list):
                for i in range(0, len(self.file_list)):
                    element = self.file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_list[i] = element.to_alipay_dict()
            if hasattr(self.file_list, 'to_alipay_dict'):
                params['file_list'] = self.file_list.to_alipay_dict()
            else:
                params['file_list'] = self.file_list
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.websites:
            if hasattr(self.websites, 'to_alipay_dict'):
                params['websites'] = self.websites.to_alipay_dict()
            else:
                params['websites'] = self.websites
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasOpenIndrbeneficiaryApplyModel()
        if 'address' in d:
            o.address = d['address']
        if 'beneficiary_abb_name' in d:
            o.beneficiary_abb_name = d['beneficiary_abb_name']
        if 'beneficiary_local_name' in d:
            o.beneficiary_local_name = d['beneficiary_local_name']
        if 'beneficiary_name' in d:
            o.beneficiary_name = d['beneficiary_name']
        if 'beneficiary_sub_type' in d:
            o.beneficiary_sub_type = d['beneficiary_sub_type']
        if 'beneficiary_type' in d:
            o.beneficiary_type = d['beneficiary_type']
        if 'email' in d:
            o.email = d['email']
        if 'file_list' in d:
            o.file_list = d['file_list']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'remark' in d:
            o.remark = d['remark']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'websites' in d:
            o.websites = d['websites']
        return o


