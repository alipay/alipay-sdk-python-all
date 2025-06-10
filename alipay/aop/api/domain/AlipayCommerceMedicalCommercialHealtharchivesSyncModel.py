#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DentalInquiryArchivesInfo import DentalInquiryArchivesInfo


class AlipayCommerceMedicalCommercialHealtharchivesSyncModel(object):

    def __init__(self):
        self._age = None
        self._archives_type = None
        self._buyer_id = None
        self._dental_inquiry_archives_info = None
        self._gender = None
        self._open_id = None
        self._out_biz_no = None
        self._user_name = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def archives_type(self):
        return self._archives_type

    @archives_type.setter
    def archives_type(self, value):
        self._archives_type = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def dental_inquiry_archives_info(self):
        return self._dental_inquiry_archives_info

    @dental_inquiry_archives_info.setter
    def dental_inquiry_archives_info(self, value):
        if isinstance(value, DentalInquiryArchivesInfo):
            self._dental_inquiry_archives_info = value
        else:
            self._dental_inquiry_archives_info = DentalInquiryArchivesInfo.from_alipay_dict(value)
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.archives_type:
            if hasattr(self.archives_type, 'to_alipay_dict'):
                params['archives_type'] = self.archives_type.to_alipay_dict()
            else:
                params['archives_type'] = self.archives_type
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.dental_inquiry_archives_info:
            if hasattr(self.dental_inquiry_archives_info, 'to_alipay_dict'):
                params['dental_inquiry_archives_info'] = self.dental_inquiry_archives_info.to_alipay_dict()
            else:
                params['dental_inquiry_archives_info'] = self.dental_inquiry_archives_info
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        o = AlipayCommerceMedicalCommercialHealtharchivesSyncModel()
        if 'age' in d:
            o.age = d['age']
        if 'archives_type' in d:
            o.archives_type = d['archives_type']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'dental_inquiry_archives_info' in d:
            o.dental_inquiry_archives_info = d['dental_inquiry_archives_info']
        if 'gender' in d:
            o.gender = d['gender']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


