#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BizParamKeyValue import BizParamKeyValue


class PassInstanceDetail(object):

    def __init__(self):
        self._biz_param_list = None
        self._channel_id = None
        self._create_time = None
        self._end_date = None
        self._is_deleted = None
        self._logo = None
        self._logo_text = None
        self._modify_time = None
        self._pass_id = None
        self._product = None
        self._serial_number = None
        self._start_date = None
        self._status = None
        self._strip = None
        self._tpl_id = None
        self._type = None
        self._user_id = None

    @property
    def biz_param_list(self):
        return self._biz_param_list

    @biz_param_list.setter
    def biz_param_list(self, value):
        if isinstance(value, list):
            self._biz_param_list = list()
            for i in value:
                if isinstance(i, BizParamKeyValue):
                    self._biz_param_list.append(i)
                else:
                    self._biz_param_list.append(BizParamKeyValue.from_alipay_dict(i))
    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def is_deleted(self):
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, value):
        self._is_deleted = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def logo_text(self):
        return self._logo_text

    @logo_text.setter
    def logo_text(self, value):
        self._logo_text = value
    @property
    def modify_time(self):
        return self._modify_time

    @modify_time.setter
    def modify_time(self, value):
        self._modify_time = value
    @property
    def pass_id(self):
        return self._pass_id

    @pass_id.setter
    def pass_id(self, value):
        self._pass_id = value
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        self._serial_number = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def strip(self):
        return self._strip

    @strip.setter
    def strip(self, value):
        self._strip = value
    @property
    def tpl_id(self):
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, value):
        self._tpl_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_param_list:
            if isinstance(self.biz_param_list, list):
                for i in range(0, len(self.biz_param_list)):
                    element = self.biz_param_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_param_list[i] = element.to_alipay_dict()
            if hasattr(self.biz_param_list, 'to_alipay_dict'):
                params['biz_param_list'] = self.biz_param_list.to_alipay_dict()
            else:
                params['biz_param_list'] = self.biz_param_list
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.is_deleted:
            if hasattr(self.is_deleted, 'to_alipay_dict'):
                params['is_deleted'] = self.is_deleted.to_alipay_dict()
            else:
                params['is_deleted'] = self.is_deleted
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.logo_text:
            if hasattr(self.logo_text, 'to_alipay_dict'):
                params['logo_text'] = self.logo_text.to_alipay_dict()
            else:
                params['logo_text'] = self.logo_text
        if self.modify_time:
            if hasattr(self.modify_time, 'to_alipay_dict'):
                params['modify_time'] = self.modify_time.to_alipay_dict()
            else:
                params['modify_time'] = self.modify_time
        if self.pass_id:
            if hasattr(self.pass_id, 'to_alipay_dict'):
                params['pass_id'] = self.pass_id.to_alipay_dict()
            else:
                params['pass_id'] = self.pass_id
        if self.product:
            if hasattr(self.product, 'to_alipay_dict'):
                params['product'] = self.product.to_alipay_dict()
            else:
                params['product'] = self.product
        if self.serial_number:
            if hasattr(self.serial_number, 'to_alipay_dict'):
                params['serial_number'] = self.serial_number.to_alipay_dict()
            else:
                params['serial_number'] = self.serial_number
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.strip:
            if hasattr(self.strip, 'to_alipay_dict'):
                params['strip'] = self.strip.to_alipay_dict()
            else:
                params['strip'] = self.strip
        if self.tpl_id:
            if hasattr(self.tpl_id, 'to_alipay_dict'):
                params['tpl_id'] = self.tpl_id.to_alipay_dict()
            else:
                params['tpl_id'] = self.tpl_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PassInstanceDetail()
        if 'biz_param_list' in d:
            o.biz_param_list = d['biz_param_list']
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'is_deleted' in d:
            o.is_deleted = d['is_deleted']
        if 'logo' in d:
            o.logo = d['logo']
        if 'logo_text' in d:
            o.logo_text = d['logo_text']
        if 'modify_time' in d:
            o.modify_time = d['modify_time']
        if 'pass_id' in d:
            o.pass_id = d['pass_id']
        if 'product' in d:
            o.product = d['product']
        if 'serial_number' in d:
            o.serial_number = d['serial_number']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'status' in d:
            o.status = d['status']
        if 'strip' in d:
            o.strip = d['strip']
        if 'tpl_id' in d:
            o.tpl_id = d['tpl_id']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


