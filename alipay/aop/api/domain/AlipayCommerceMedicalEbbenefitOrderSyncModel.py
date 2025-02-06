#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalEbbenefitOrderSyncModel(object):

    def __init__(self):
        self._company_id = None
        self._doctor_avatar_url = None
        self._doctor_department = None
        self._doctor_education_title = None
        self._doctor_hospital = None
        self._doctor_hospital_level = None
        self._doctor_name = None
        self._doctor_title = None
        self._eb_user_id = None
        self._inquiry_mode = None
        self._member_age = None
        self._member_id = None
        self._order_create_time = None
        self._order_detail_url = None
        self._order_id = None
        self._order_im_url = None
        self._order_status = None
        self._order_type = None
        self._out_doctor_id = None
        self._out_member_id = None
        self._out_order_id = None
        self._out_parent_order_id = None
        self._out_sub_user_id = None
        self._out_user_id = None
        self._product_id = None
        self._provide_company_id = None
        self._self_funded = None
        self._sync_type = None

    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, value):
        self._company_id = value
    @property
    def doctor_avatar_url(self):
        return self._doctor_avatar_url

    @doctor_avatar_url.setter
    def doctor_avatar_url(self, value):
        self._doctor_avatar_url = value
    @property
    def doctor_department(self):
        return self._doctor_department

    @doctor_department.setter
    def doctor_department(self, value):
        self._doctor_department = value
    @property
    def doctor_education_title(self):
        return self._doctor_education_title

    @doctor_education_title.setter
    def doctor_education_title(self, value):
        self._doctor_education_title = value
    @property
    def doctor_hospital(self):
        return self._doctor_hospital

    @doctor_hospital.setter
    def doctor_hospital(self, value):
        self._doctor_hospital = value
    @property
    def doctor_hospital_level(self):
        return self._doctor_hospital_level

    @doctor_hospital_level.setter
    def doctor_hospital_level(self, value):
        self._doctor_hospital_level = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def doctor_title(self):
        return self._doctor_title

    @doctor_title.setter
    def doctor_title(self, value):
        self._doctor_title = value
    @property
    def eb_user_id(self):
        return self._eb_user_id

    @eb_user_id.setter
    def eb_user_id(self, value):
        self._eb_user_id = value
    @property
    def inquiry_mode(self):
        return self._inquiry_mode

    @inquiry_mode.setter
    def inquiry_mode(self, value):
        self._inquiry_mode = value
    @property
    def member_age(self):
        return self._member_age

    @member_age.setter
    def member_age(self, value):
        self._member_age = value
    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_detail_url(self):
        return self._order_detail_url

    @order_detail_url.setter
    def order_detail_url(self, value):
        self._order_detail_url = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_im_url(self):
        return self._order_im_url

    @order_im_url.setter
    def order_im_url(self, value):
        self._order_im_url = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_doctor_id(self):
        return self._out_doctor_id

    @out_doctor_id.setter
    def out_doctor_id(self, value):
        self._out_doctor_id = value
    @property
    def out_member_id(self):
        return self._out_member_id

    @out_member_id.setter
    def out_member_id(self, value):
        self._out_member_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_parent_order_id(self):
        return self._out_parent_order_id

    @out_parent_order_id.setter
    def out_parent_order_id(self, value):
        self._out_parent_order_id = value
    @property
    def out_sub_user_id(self):
        return self._out_sub_user_id

    @out_sub_user_id.setter
    def out_sub_user_id(self, value):
        self._out_sub_user_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def provide_company_id(self):
        return self._provide_company_id

    @provide_company_id.setter
    def provide_company_id(self, value):
        self._provide_company_id = value
    @property
    def self_funded(self):
        return self._self_funded

    @self_funded.setter
    def self_funded(self, value):
        self._self_funded = value
    @property
    def sync_type(self):
        return self._sync_type

    @sync_type.setter
    def sync_type(self, value):
        self._sync_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_id:
            if hasattr(self.company_id, 'to_alipay_dict'):
                params['company_id'] = self.company_id.to_alipay_dict()
            else:
                params['company_id'] = self.company_id
        if self.doctor_avatar_url:
            if hasattr(self.doctor_avatar_url, 'to_alipay_dict'):
                params['doctor_avatar_url'] = self.doctor_avatar_url.to_alipay_dict()
            else:
                params['doctor_avatar_url'] = self.doctor_avatar_url
        if self.doctor_department:
            if hasattr(self.doctor_department, 'to_alipay_dict'):
                params['doctor_department'] = self.doctor_department.to_alipay_dict()
            else:
                params['doctor_department'] = self.doctor_department
        if self.doctor_education_title:
            if hasattr(self.doctor_education_title, 'to_alipay_dict'):
                params['doctor_education_title'] = self.doctor_education_title.to_alipay_dict()
            else:
                params['doctor_education_title'] = self.doctor_education_title
        if self.doctor_hospital:
            if hasattr(self.doctor_hospital, 'to_alipay_dict'):
                params['doctor_hospital'] = self.doctor_hospital.to_alipay_dict()
            else:
                params['doctor_hospital'] = self.doctor_hospital
        if self.doctor_hospital_level:
            if hasattr(self.doctor_hospital_level, 'to_alipay_dict'):
                params['doctor_hospital_level'] = self.doctor_hospital_level.to_alipay_dict()
            else:
                params['doctor_hospital_level'] = self.doctor_hospital_level
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.doctor_title:
            if hasattr(self.doctor_title, 'to_alipay_dict'):
                params['doctor_title'] = self.doctor_title.to_alipay_dict()
            else:
                params['doctor_title'] = self.doctor_title
        if self.eb_user_id:
            if hasattr(self.eb_user_id, 'to_alipay_dict'):
                params['eb_user_id'] = self.eb_user_id.to_alipay_dict()
            else:
                params['eb_user_id'] = self.eb_user_id
        if self.inquiry_mode:
            if hasattr(self.inquiry_mode, 'to_alipay_dict'):
                params['inquiry_mode'] = self.inquiry_mode.to_alipay_dict()
            else:
                params['inquiry_mode'] = self.inquiry_mode
        if self.member_age:
            if hasattr(self.member_age, 'to_alipay_dict'):
                params['member_age'] = self.member_age.to_alipay_dict()
            else:
                params['member_age'] = self.member_age
        if self.member_id:
            if hasattr(self.member_id, 'to_alipay_dict'):
                params['member_id'] = self.member_id.to_alipay_dict()
            else:
                params['member_id'] = self.member_id
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_detail_url:
            if hasattr(self.order_detail_url, 'to_alipay_dict'):
                params['order_detail_url'] = self.order_detail_url.to_alipay_dict()
            else:
                params['order_detail_url'] = self.order_detail_url
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_im_url:
            if hasattr(self.order_im_url, 'to_alipay_dict'):
                params['order_im_url'] = self.order_im_url.to_alipay_dict()
            else:
                params['order_im_url'] = self.order_im_url
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_doctor_id:
            if hasattr(self.out_doctor_id, 'to_alipay_dict'):
                params['out_doctor_id'] = self.out_doctor_id.to_alipay_dict()
            else:
                params['out_doctor_id'] = self.out_doctor_id
        if self.out_member_id:
            if hasattr(self.out_member_id, 'to_alipay_dict'):
                params['out_member_id'] = self.out_member_id.to_alipay_dict()
            else:
                params['out_member_id'] = self.out_member_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.out_parent_order_id:
            if hasattr(self.out_parent_order_id, 'to_alipay_dict'):
                params['out_parent_order_id'] = self.out_parent_order_id.to_alipay_dict()
            else:
                params['out_parent_order_id'] = self.out_parent_order_id
        if self.out_sub_user_id:
            if hasattr(self.out_sub_user_id, 'to_alipay_dict'):
                params['out_sub_user_id'] = self.out_sub_user_id.to_alipay_dict()
            else:
                params['out_sub_user_id'] = self.out_sub_user_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.provide_company_id:
            if hasattr(self.provide_company_id, 'to_alipay_dict'):
                params['provide_company_id'] = self.provide_company_id.to_alipay_dict()
            else:
                params['provide_company_id'] = self.provide_company_id
        if self.self_funded:
            if hasattr(self.self_funded, 'to_alipay_dict'):
                params['self_funded'] = self.self_funded.to_alipay_dict()
            else:
                params['self_funded'] = self.self_funded
        if self.sync_type:
            if hasattr(self.sync_type, 'to_alipay_dict'):
                params['sync_type'] = self.sync_type.to_alipay_dict()
            else:
                params['sync_type'] = self.sync_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalEbbenefitOrderSyncModel()
        if 'company_id' in d:
            o.company_id = d['company_id']
        if 'doctor_avatar_url' in d:
            o.doctor_avatar_url = d['doctor_avatar_url']
        if 'doctor_department' in d:
            o.doctor_department = d['doctor_department']
        if 'doctor_education_title' in d:
            o.doctor_education_title = d['doctor_education_title']
        if 'doctor_hospital' in d:
            o.doctor_hospital = d['doctor_hospital']
        if 'doctor_hospital_level' in d:
            o.doctor_hospital_level = d['doctor_hospital_level']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'doctor_title' in d:
            o.doctor_title = d['doctor_title']
        if 'eb_user_id' in d:
            o.eb_user_id = d['eb_user_id']
        if 'inquiry_mode' in d:
            o.inquiry_mode = d['inquiry_mode']
        if 'member_age' in d:
            o.member_age = d['member_age']
        if 'member_id' in d:
            o.member_id = d['member_id']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_detail_url' in d:
            o.order_detail_url = d['order_detail_url']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_im_url' in d:
            o.order_im_url = d['order_im_url']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_doctor_id' in d:
            o.out_doctor_id = d['out_doctor_id']
        if 'out_member_id' in d:
            o.out_member_id = d['out_member_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_parent_order_id' in d:
            o.out_parent_order_id = d['out_parent_order_id']
        if 'out_sub_user_id' in d:
            o.out_sub_user_id = d['out_sub_user_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'provide_company_id' in d:
            o.provide_company_id = d['provide_company_id']
        if 'self_funded' in d:
            o.self_funded = d['self_funded']
        if 'sync_type' in d:
            o.sync_type = d['sync_type']
        return o


