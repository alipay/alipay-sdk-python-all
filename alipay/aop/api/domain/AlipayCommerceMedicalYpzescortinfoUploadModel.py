#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalYpzescortinfoUploadModel(object):

    def __init__(self):
        self._alipay_open_id = None
        self._alipay_user_id = None
        self._biz_id = None
        self._biz_timestamp = None
        self._escort_avatar_url = None
        self._escort_cert_no = None
        self._escort_cert_type = None
        self._escort_id = None
        self._escort_name = None
        self._escort_phone = None
        self._escort_service_time = None
        self._escort_tag_list = None
        self._order_id = None
        self._order_source = None
        self._org_id = None
        self._service_provider = None
        self._status = None
        self._table_type = None
        self._uscc = None

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
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_timestamp(self):
        return self._biz_timestamp

    @biz_timestamp.setter
    def biz_timestamp(self, value):
        self._biz_timestamp = value
    @property
    def escort_avatar_url(self):
        return self._escort_avatar_url

    @escort_avatar_url.setter
    def escort_avatar_url(self, value):
        self._escort_avatar_url = value
    @property
    def escort_cert_no(self):
        return self._escort_cert_no

    @escort_cert_no.setter
    def escort_cert_no(self, value):
        self._escort_cert_no = value
    @property
    def escort_cert_type(self):
        return self._escort_cert_type

    @escort_cert_type.setter
    def escort_cert_type(self, value):
        self._escort_cert_type = value
    @property
    def escort_id(self):
        return self._escort_id

    @escort_id.setter
    def escort_id(self, value):
        self._escort_id = value
    @property
    def escort_name(self):
        return self._escort_name

    @escort_name.setter
    def escort_name(self, value):
        self._escort_name = value
    @property
    def escort_phone(self):
        return self._escort_phone

    @escort_phone.setter
    def escort_phone(self, value):
        self._escort_phone = value
    @property
    def escort_service_time(self):
        return self._escort_service_time

    @escort_service_time.setter
    def escort_service_time(self, value):
        self._escort_service_time = value
    @property
    def escort_tag_list(self):
        return self._escort_tag_list

    @escort_tag_list.setter
    def escort_tag_list(self, value):
        self._escort_tag_list = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_source(self):
        return self._order_source

    @order_source.setter
    def order_source(self, value):
        self._order_source = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def service_provider(self):
        return self._service_provider

    @service_provider.setter
    def service_provider(self, value):
        self._service_provider = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def table_type(self):
        return self._table_type

    @table_type.setter
    def table_type(self, value):
        self._table_type = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value


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
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_timestamp:
            if hasattr(self.biz_timestamp, 'to_alipay_dict'):
                params['biz_timestamp'] = self.biz_timestamp.to_alipay_dict()
            else:
                params['biz_timestamp'] = self.biz_timestamp
        if self.escort_avatar_url:
            if hasattr(self.escort_avatar_url, 'to_alipay_dict'):
                params['escort_avatar_url'] = self.escort_avatar_url.to_alipay_dict()
            else:
                params['escort_avatar_url'] = self.escort_avatar_url
        if self.escort_cert_no:
            if hasattr(self.escort_cert_no, 'to_alipay_dict'):
                params['escort_cert_no'] = self.escort_cert_no.to_alipay_dict()
            else:
                params['escort_cert_no'] = self.escort_cert_no
        if self.escort_cert_type:
            if hasattr(self.escort_cert_type, 'to_alipay_dict'):
                params['escort_cert_type'] = self.escort_cert_type.to_alipay_dict()
            else:
                params['escort_cert_type'] = self.escort_cert_type
        if self.escort_id:
            if hasattr(self.escort_id, 'to_alipay_dict'):
                params['escort_id'] = self.escort_id.to_alipay_dict()
            else:
                params['escort_id'] = self.escort_id
        if self.escort_name:
            if hasattr(self.escort_name, 'to_alipay_dict'):
                params['escort_name'] = self.escort_name.to_alipay_dict()
            else:
                params['escort_name'] = self.escort_name
        if self.escort_phone:
            if hasattr(self.escort_phone, 'to_alipay_dict'):
                params['escort_phone'] = self.escort_phone.to_alipay_dict()
            else:
                params['escort_phone'] = self.escort_phone
        if self.escort_service_time:
            if hasattr(self.escort_service_time, 'to_alipay_dict'):
                params['escort_service_time'] = self.escort_service_time.to_alipay_dict()
            else:
                params['escort_service_time'] = self.escort_service_time
        if self.escort_tag_list:
            if hasattr(self.escort_tag_list, 'to_alipay_dict'):
                params['escort_tag_list'] = self.escort_tag_list.to_alipay_dict()
            else:
                params['escort_tag_list'] = self.escort_tag_list
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_source:
            if hasattr(self.order_source, 'to_alipay_dict'):
                params['order_source'] = self.order_source.to_alipay_dict()
            else:
                params['order_source'] = self.order_source
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.service_provider:
            if hasattr(self.service_provider, 'to_alipay_dict'):
                params['service_provider'] = self.service_provider.to_alipay_dict()
            else:
                params['service_provider'] = self.service_provider
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.table_type:
            if hasattr(self.table_type, 'to_alipay_dict'):
                params['table_type'] = self.table_type.to_alipay_dict()
            else:
                params['table_type'] = self.table_type
        if self.uscc:
            if hasattr(self.uscc, 'to_alipay_dict'):
                params['uscc'] = self.uscc.to_alipay_dict()
            else:
                params['uscc'] = self.uscc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalYpzescortinfoUploadModel()
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_timestamp' in d:
            o.biz_timestamp = d['biz_timestamp']
        if 'escort_avatar_url' in d:
            o.escort_avatar_url = d['escort_avatar_url']
        if 'escort_cert_no' in d:
            o.escort_cert_no = d['escort_cert_no']
        if 'escort_cert_type' in d:
            o.escort_cert_type = d['escort_cert_type']
        if 'escort_id' in d:
            o.escort_id = d['escort_id']
        if 'escort_name' in d:
            o.escort_name = d['escort_name']
        if 'escort_phone' in d:
            o.escort_phone = d['escort_phone']
        if 'escort_service_time' in d:
            o.escort_service_time = d['escort_service_time']
        if 'escort_tag_list' in d:
            o.escort_tag_list = d['escort_tag_list']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_source' in d:
            o.order_source = d['order_source']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'service_provider' in d:
            o.service_provider = d['service_provider']
        if 'status' in d:
            o.status = d['status']
        if 'table_type' in d:
            o.table_type = d['table_type']
        if 'uscc' in d:
            o.uscc = d['uscc']
        return o


