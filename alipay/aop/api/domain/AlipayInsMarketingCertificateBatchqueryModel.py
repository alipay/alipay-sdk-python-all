#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsMarketingCertificateBatchqueryModel(object):

    def __init__(self):
        self._certificate_no = None
        self._certificate_type = None
        self._current_page_no = None
        self._effect_time = None
        self._inst_id = None
        self._is_enabled = None
        self._order_id = None
        self._order_source = None
        self._out_biz_no = None
        self._owner_uid = None
        self._page_size = None
        self._status = None

    @property
    def certificate_no(self):
        return self._certificate_no

    @certificate_no.setter
    def certificate_no(self, value):
        self._certificate_no = value
    @property
    def certificate_type(self):
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, value):
        self._certificate_type = value
    @property
    def current_page_no(self):
        return self._current_page_no

    @current_page_no.setter
    def current_page_no(self, value):
        self._current_page_no = value
    @property
    def effect_time(self):
        return self._effect_time

    @effect_time.setter
    def effect_time(self, value):
        self._effect_time = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def is_enabled(self):
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, value):
        self._is_enabled = value
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
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def owner_uid(self):
        return self._owner_uid

    @owner_uid.setter
    def owner_uid(self, value):
        self._owner_uid = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_no:
            if hasattr(self.certificate_no, 'to_alipay_dict'):
                params['certificate_no'] = self.certificate_no.to_alipay_dict()
            else:
                params['certificate_no'] = self.certificate_no
        if self.certificate_type:
            if hasattr(self.certificate_type, 'to_alipay_dict'):
                params['certificate_type'] = self.certificate_type.to_alipay_dict()
            else:
                params['certificate_type'] = self.certificate_type
        if self.current_page_no:
            if hasattr(self.current_page_no, 'to_alipay_dict'):
                params['current_page_no'] = self.current_page_no.to_alipay_dict()
            else:
                params['current_page_no'] = self.current_page_no
        if self.effect_time:
            if hasattr(self.effect_time, 'to_alipay_dict'):
                params['effect_time'] = self.effect_time.to_alipay_dict()
            else:
                params['effect_time'] = self.effect_time
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.is_enabled:
            if hasattr(self.is_enabled, 'to_alipay_dict'):
                params['is_enabled'] = self.is_enabled.to_alipay_dict()
            else:
                params['is_enabled'] = self.is_enabled
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
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.owner_uid:
            if hasattr(self.owner_uid, 'to_alipay_dict'):
                params['owner_uid'] = self.owner_uid.to_alipay_dict()
            else:
                params['owner_uid'] = self.owner_uid
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsMarketingCertificateBatchqueryModel()
        if 'certificate_no' in d:
            o.certificate_no = d['certificate_no']
        if 'certificate_type' in d:
            o.certificate_type = d['certificate_type']
        if 'current_page_no' in d:
            o.current_page_no = d['current_page_no']
        if 'effect_time' in d:
            o.effect_time = d['effect_time']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'is_enabled' in d:
            o.is_enabled = d['is_enabled']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_source' in d:
            o.order_source = d['order_source']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'owner_uid' in d:
            o.owner_uid = d['owner_uid']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'status' in d:
            o.status = d['status']
        return o


