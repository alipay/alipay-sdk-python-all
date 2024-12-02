#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PlatformInquiryOrderExtInfo import PlatformInquiryOrderExtInfo


class AlipayCommerceMedicalIndustrydataInquiryorderSyncModel(object):

    def __init__(self):
        self._alipay_open_id = None
        self._alipay_trade_no = None
        self._alipay_user_id = None
        self._amount = None
        self._department_name = None
        self._doctor_name = None
        self._ext_info = None
        self._ext_shift_case_id = None
        self._hospital_name = None
        self._inquiry_mode = None
        self._inquiry_type = None
        self._merchant_doctor_id = None
        self._merchant_order_link_page = None
        self._merchant_order_status = None
        self._merchant_user_id = None
        self._order_create_time = None
        self._order_hidden_flag = None
        self._order_modified_time = None
        self._order_type = None
        self._out_biz_no = None
        self._out_biz_type = None
        self._patient_age = None
        self._patient_idcard = None
        self._patient_name = None
        self._patient_phone = None
        self._patient_sex = None
        self._platform_code = None
        self._real_amount = None
        self._refund_amount = None
        self._scheduled_time = None

    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, PlatformInquiryOrderExtInfo):
            self._ext_info = value
        else:
            self._ext_info = PlatformInquiryOrderExtInfo.from_alipay_dict(value)
    @property
    def ext_shift_case_id(self):
        return self._ext_shift_case_id

    @ext_shift_case_id.setter
    def ext_shift_case_id(self, value):
        self._ext_shift_case_id = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def inquiry_mode(self):
        return self._inquiry_mode

    @inquiry_mode.setter
    def inquiry_mode(self, value):
        self._inquiry_mode = value
    @property
    def inquiry_type(self):
        return self._inquiry_type

    @inquiry_type.setter
    def inquiry_type(self, value):
        self._inquiry_type = value
    @property
    def merchant_doctor_id(self):
        return self._merchant_doctor_id

    @merchant_doctor_id.setter
    def merchant_doctor_id(self, value):
        self._merchant_doctor_id = value
    @property
    def merchant_order_link_page(self):
        return self._merchant_order_link_page

    @merchant_order_link_page.setter
    def merchant_order_link_page(self, value):
        self._merchant_order_link_page = value
    @property
    def merchant_order_status(self):
        return self._merchant_order_status

    @merchant_order_status.setter
    def merchant_order_status(self, value):
        self._merchant_order_status = value
    @property
    def merchant_user_id(self):
        return self._merchant_user_id

    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_hidden_flag(self):
        return self._order_hidden_flag

    @order_hidden_flag.setter
    def order_hidden_flag(self, value):
        self._order_hidden_flag = value
    @property
    def order_modified_time(self):
        return self._order_modified_time

    @order_modified_time.setter
    def order_modified_time(self, value):
        self._order_modified_time = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value
    @property
    def patient_age(self):
        return self._patient_age

    @patient_age.setter
    def patient_age(self, value):
        self._patient_age = value
    @property
    def patient_idcard(self):
        return self._patient_idcard

    @patient_idcard.setter
    def patient_idcard(self, value):
        self._patient_idcard = value
    @property
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    def patient_name(self, value):
        self._patient_name = value
    @property
    def patient_phone(self):
        return self._patient_phone

    @patient_phone.setter
    def patient_phone(self, value):
        self._patient_phone = value
    @property
    def patient_sex(self):
        return self._patient_sex

    @patient_sex.setter
    def patient_sex(self, value):
        self._patient_sex = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def scheduled_time(self):
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, value):
        self._scheduled_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.alipay_trade_no:
            if hasattr(self.alipay_trade_no, 'to_alipay_dict'):
                params['alipay_trade_no'] = self.alipay_trade_no.to_alipay_dict()
            else:
                params['alipay_trade_no'] = self.alipay_trade_no
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.department_name:
            if hasattr(self.department_name, 'to_alipay_dict'):
                params['department_name'] = self.department_name.to_alipay_dict()
            else:
                params['department_name'] = self.department_name
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.ext_shift_case_id:
            if hasattr(self.ext_shift_case_id, 'to_alipay_dict'):
                params['ext_shift_case_id'] = self.ext_shift_case_id.to_alipay_dict()
            else:
                params['ext_shift_case_id'] = self.ext_shift_case_id
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.inquiry_mode:
            if hasattr(self.inquiry_mode, 'to_alipay_dict'):
                params['inquiry_mode'] = self.inquiry_mode.to_alipay_dict()
            else:
                params['inquiry_mode'] = self.inquiry_mode
        if self.inquiry_type:
            if hasattr(self.inquiry_type, 'to_alipay_dict'):
                params['inquiry_type'] = self.inquiry_type.to_alipay_dict()
            else:
                params['inquiry_type'] = self.inquiry_type
        if self.merchant_doctor_id:
            if hasattr(self.merchant_doctor_id, 'to_alipay_dict'):
                params['merchant_doctor_id'] = self.merchant_doctor_id.to_alipay_dict()
            else:
                params['merchant_doctor_id'] = self.merchant_doctor_id
        if self.merchant_order_link_page:
            if hasattr(self.merchant_order_link_page, 'to_alipay_dict'):
                params['merchant_order_link_page'] = self.merchant_order_link_page.to_alipay_dict()
            else:
                params['merchant_order_link_page'] = self.merchant_order_link_page
        if self.merchant_order_status:
            if hasattr(self.merchant_order_status, 'to_alipay_dict'):
                params['merchant_order_status'] = self.merchant_order_status.to_alipay_dict()
            else:
                params['merchant_order_status'] = self.merchant_order_status
        if self.merchant_user_id:
            if hasattr(self.merchant_user_id, 'to_alipay_dict'):
                params['merchant_user_id'] = self.merchant_user_id.to_alipay_dict()
            else:
                params['merchant_user_id'] = self.merchant_user_id
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_hidden_flag:
            if hasattr(self.order_hidden_flag, 'to_alipay_dict'):
                params['order_hidden_flag'] = self.order_hidden_flag.to_alipay_dict()
            else:
                params['order_hidden_flag'] = self.order_hidden_flag
        if self.order_modified_time:
            if hasattr(self.order_modified_time, 'to_alipay_dict'):
                params['order_modified_time'] = self.order_modified_time.to_alipay_dict()
            else:
                params['order_modified_time'] = self.order_modified_time
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        if self.patient_age:
            if hasattr(self.patient_age, 'to_alipay_dict'):
                params['patient_age'] = self.patient_age.to_alipay_dict()
            else:
                params['patient_age'] = self.patient_age
        if self.patient_idcard:
            if hasattr(self.patient_idcard, 'to_alipay_dict'):
                params['patient_idcard'] = self.patient_idcard.to_alipay_dict()
            else:
                params['patient_idcard'] = self.patient_idcard
        if self.patient_name:
            if hasattr(self.patient_name, 'to_alipay_dict'):
                params['patient_name'] = self.patient_name.to_alipay_dict()
            else:
                params['patient_name'] = self.patient_name
        if self.patient_phone:
            if hasattr(self.patient_phone, 'to_alipay_dict'):
                params['patient_phone'] = self.patient_phone.to_alipay_dict()
            else:
                params['patient_phone'] = self.patient_phone
        if self.patient_sex:
            if hasattr(self.patient_sex, 'to_alipay_dict'):
                params['patient_sex'] = self.patient_sex.to_alipay_dict()
            else:
                params['patient_sex'] = self.patient_sex
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.scheduled_time:
            if hasattr(self.scheduled_time, 'to_alipay_dict'):
                params['scheduled_time'] = self.scheduled_time.to_alipay_dict()
            else:
                params['scheduled_time'] = self.scheduled_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataInquiryorderSyncModel()
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_trade_no' in d:
            o.alipay_trade_no = d['alipay_trade_no']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'amount' in d:
            o.amount = d['amount']
        if 'department_name' in d:
            o.department_name = d['department_name']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'ext_shift_case_id' in d:
            o.ext_shift_case_id = d['ext_shift_case_id']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'inquiry_mode' in d:
            o.inquiry_mode = d['inquiry_mode']
        if 'inquiry_type' in d:
            o.inquiry_type = d['inquiry_type']
        if 'merchant_doctor_id' in d:
            o.merchant_doctor_id = d['merchant_doctor_id']
        if 'merchant_order_link_page' in d:
            o.merchant_order_link_page = d['merchant_order_link_page']
        if 'merchant_order_status' in d:
            o.merchant_order_status = d['merchant_order_status']
        if 'merchant_user_id' in d:
            o.merchant_user_id = d['merchant_user_id']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_hidden_flag' in d:
            o.order_hidden_flag = d['order_hidden_flag']
        if 'order_modified_time' in d:
            o.order_modified_time = d['order_modified_time']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        if 'patient_age' in d:
            o.patient_age = d['patient_age']
        if 'patient_idcard' in d:
            o.patient_idcard = d['patient_idcard']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'patient_phone' in d:
            o.patient_phone = d['patient_phone']
        if 'patient_sex' in d:
            o.patient_sex = d['patient_sex']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'scheduled_time' in d:
            o.scheduled_time = d['scheduled_time']
        return o


