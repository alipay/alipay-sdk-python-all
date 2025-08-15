#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalMsgUnifiedSendModel(object):

    def __init__(self):
        self._alipay_open_id = None
        self._alipay_user_id = None
        self._api_service = None
        self._ext_info = None
        self._ext_params = None
        self._hospital_code = None
        self._hospital_name = None
        self._merchant_order_status = None
        self._message_channel = None
        self._order_create_time = None
        self._order_modified_time = None
        self._org_name = None
        self._out_biz_no = None
        self._out_biz_type = None
        self._template_code = None
        self._uscc = None
        self._user_card_no = None
        self._user_card_type = None

    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def api_service(self):
        return self._api_service

    @api_service.setter
    def api_service(self, value):
        self._api_service = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        self._ext_params = value
    @property
    def hospital_code(self):
        return self._hospital_code

    @hospital_code.setter
    def hospital_code(self, value):
        self._hospital_code = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def merchant_order_status(self):
        return self._merchant_order_status

    @merchant_order_status.setter
    def merchant_order_status(self, value):
        self._merchant_order_status = value
    @property
    def message_channel(self):
        return self._message_channel

    @message_channel.setter
    def message_channel(self, value):
        self._message_channel = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_modified_time(self):
        return self._order_modified_time

    @order_modified_time.setter
    def order_modified_time(self, value):
        self._order_modified_time = value
    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
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
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value
    @property
    def user_card_no(self):
        return self._user_card_no

    @user_card_no.setter
    def user_card_no(self, value):
        self._user_card_no = value
    @property
    def user_card_type(self):
        return self._user_card_type

    @user_card_type.setter
    def user_card_type(self, value):
        self._user_card_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.api_service:
            if hasattr(self.api_service, 'to_alipay_dict'):
                params['api_service'] = self.api_service.to_alipay_dict()
            else:
                params['api_service'] = self.api_service
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.ext_params:
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
        if self.hospital_code:
            if hasattr(self.hospital_code, 'to_alipay_dict'):
                params['hospital_code'] = self.hospital_code.to_alipay_dict()
            else:
                params['hospital_code'] = self.hospital_code
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.merchant_order_status:
            if hasattr(self.merchant_order_status, 'to_alipay_dict'):
                params['merchant_order_status'] = self.merchant_order_status.to_alipay_dict()
            else:
                params['merchant_order_status'] = self.merchant_order_status
        if self.message_channel:
            if hasattr(self.message_channel, 'to_alipay_dict'):
                params['message_channel'] = self.message_channel.to_alipay_dict()
            else:
                params['message_channel'] = self.message_channel
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_modified_time:
            if hasattr(self.order_modified_time, 'to_alipay_dict'):
                params['order_modified_time'] = self.order_modified_time.to_alipay_dict()
            else:
                params['order_modified_time'] = self.order_modified_time
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
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
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.uscc:
            if hasattr(self.uscc, 'to_alipay_dict'):
                params['uscc'] = self.uscc.to_alipay_dict()
            else:
                params['uscc'] = self.uscc
        if self.user_card_no:
            if hasattr(self.user_card_no, 'to_alipay_dict'):
                params['user_card_no'] = self.user_card_no.to_alipay_dict()
            else:
                params['user_card_no'] = self.user_card_no
        if self.user_card_type:
            if hasattr(self.user_card_type, 'to_alipay_dict'):
                params['user_card_type'] = self.user_card_type.to_alipay_dict()
            else:
                params['user_card_type'] = self.user_card_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMsgUnifiedSendModel()
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'api_service' in d:
            o.api_service = d['api_service']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        if 'hospital_code' in d:
            o.hospital_code = d['hospital_code']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'merchant_order_status' in d:
            o.merchant_order_status = d['merchant_order_status']
        if 'message_channel' in d:
            o.message_channel = d['message_channel']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_modified_time' in d:
            o.order_modified_time = d['order_modified_time']
        if 'org_name' in d:
            o.org_name = d['org_name']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'uscc' in d:
            o.uscc = d['uscc']
        if 'user_card_no' in d:
            o.user_card_no = d['user_card_no']
        if 'user_card_type' in d:
            o.user_card_type = d['user_card_type']
        return o


