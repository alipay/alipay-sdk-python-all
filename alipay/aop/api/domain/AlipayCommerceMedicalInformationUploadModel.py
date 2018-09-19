#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInformationUploadModel(object):

    def __init__(self):
        self._auth_code = None
        self._auth_type = None
        self._body = None
        self._buyer_id = None
        self._extend_params = None
        self._gmt_out_create = None
        self._industry = None
        self._is_insurance = None
        self._medical_card_id = None
        self._medical_card_inst_id = None
        self._org_name = None
        self._org_no = None
        self._out_trade_no = None
        self._patient_card_no = None
        self._patient_card_type = None
        self._patient_mobile = None
        self._patient_name = None
        self._request_content = None
        self._scene = None
        self._seller_id = None
        self._serial_no = None
        self._subject = None
        self._total_amount = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def auth_type(self):
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        self._auth_type = value
    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def gmt_out_create(self):
        return self._gmt_out_create

    @gmt_out_create.setter
    def gmt_out_create(self, value):
        self._gmt_out_create = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def is_insurance(self):
        return self._is_insurance

    @is_insurance.setter
    def is_insurance(self, value):
        self._is_insurance = value
    @property
    def medical_card_id(self):
        return self._medical_card_id

    @medical_card_id.setter
    def medical_card_id(self, value):
        self._medical_card_id = value
    @property
    def medical_card_inst_id(self):
        return self._medical_card_inst_id

    @medical_card_inst_id.setter
    def medical_card_inst_id(self, value):
        self._medical_card_inst_id = value
    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
    @property
    def org_no(self):
        return self._org_no

    @org_no.setter
    def org_no(self, value):
        self._org_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def patient_card_no(self):
        return self._patient_card_no

    @patient_card_no.setter
    def patient_card_no(self, value):
        self._patient_card_no = value
    @property
    def patient_card_type(self):
        return self._patient_card_type

    @patient_card_type.setter
    def patient_card_type(self, value):
        self._patient_card_type = value
    @property
    def patient_mobile(self):
        return self._patient_mobile

    @patient_mobile.setter
    def patient_mobile(self, value):
        self._patient_mobile = value
    @property
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    def patient_name(self, value):
        self._patient_name = value
    @property
    def request_content(self):
        return self._request_content

    @request_content.setter
    def request_content(self, value):
        self._request_content = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.auth_type:
            if hasattr(self.auth_type, 'to_alipay_dict'):
                params['auth_type'] = self.auth_type.to_alipay_dict()
            else:
                params['auth_type'] = self.auth_type
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.gmt_out_create:
            if hasattr(self.gmt_out_create, 'to_alipay_dict'):
                params['gmt_out_create'] = self.gmt_out_create.to_alipay_dict()
            else:
                params['gmt_out_create'] = self.gmt_out_create
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.is_insurance:
            if hasattr(self.is_insurance, 'to_alipay_dict'):
                params['is_insurance'] = self.is_insurance.to_alipay_dict()
            else:
                params['is_insurance'] = self.is_insurance
        if self.medical_card_id:
            if hasattr(self.medical_card_id, 'to_alipay_dict'):
                params['medical_card_id'] = self.medical_card_id.to_alipay_dict()
            else:
                params['medical_card_id'] = self.medical_card_id
        if self.medical_card_inst_id:
            if hasattr(self.medical_card_inst_id, 'to_alipay_dict'):
                params['medical_card_inst_id'] = self.medical_card_inst_id.to_alipay_dict()
            else:
                params['medical_card_inst_id'] = self.medical_card_inst_id
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
        if self.org_no:
            if hasattr(self.org_no, 'to_alipay_dict'):
                params['org_no'] = self.org_no.to_alipay_dict()
            else:
                params['org_no'] = self.org_no
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.patient_card_no:
            if hasattr(self.patient_card_no, 'to_alipay_dict'):
                params['patient_card_no'] = self.patient_card_no.to_alipay_dict()
            else:
                params['patient_card_no'] = self.patient_card_no
        if self.patient_card_type:
            if hasattr(self.patient_card_type, 'to_alipay_dict'):
                params['patient_card_type'] = self.patient_card_type.to_alipay_dict()
            else:
                params['patient_card_type'] = self.patient_card_type
        if self.patient_mobile:
            if hasattr(self.patient_mobile, 'to_alipay_dict'):
                params['patient_mobile'] = self.patient_mobile.to_alipay_dict()
            else:
                params['patient_mobile'] = self.patient_mobile
        if self.patient_name:
            if hasattr(self.patient_name, 'to_alipay_dict'):
                params['patient_name'] = self.patient_name.to_alipay_dict()
            else:
                params['patient_name'] = self.patient_name
        if self.request_content:
            if hasattr(self.request_content, 'to_alipay_dict'):
                params['request_content'] = self.request_content.to_alipay_dict()
            else:
                params['request_content'] = self.request_content
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInformationUploadModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'auth_type' in d:
            o.auth_type = d['auth_type']
        if 'body' in d:
            o.body = d['body']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'gmt_out_create' in d:
            o.gmt_out_create = d['gmt_out_create']
        if 'industry' in d:
            o.industry = d['industry']
        if 'is_insurance' in d:
            o.is_insurance = d['is_insurance']
        if 'medical_card_id' in d:
            o.medical_card_id = d['medical_card_id']
        if 'medical_card_inst_id' in d:
            o.medical_card_inst_id = d['medical_card_inst_id']
        if 'org_name' in d:
            o.org_name = d['org_name']
        if 'org_no' in d:
            o.org_no = d['org_no']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'patient_card_no' in d:
            o.patient_card_no = d['patient_card_no']
        if 'patient_card_type' in d:
            o.patient_card_type = d['patient_card_type']
        if 'patient_mobile' in d:
            o.patient_mobile = d['patient_mobile']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'request_content' in d:
            o.request_content = d['request_content']
        if 'scene' in d:
            o.scene = d['scene']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'subject' in d:
            o.subject = d['subject']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


