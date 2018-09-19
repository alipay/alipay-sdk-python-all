#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InboundOrderVO(object):

    def __init__(self):
        self._ext_info = None
        self._gmt_create = None
        self._gmt_modified = None
        self._inbound_order_id = None
        self._inbound_type = None
        self._notice_date = None
        self._operator_id = None
        self._operator_type = None
        self._out_biz_no = None
        self._status = None
        self._warehouse_code = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def inbound_order_id(self):
        return self._inbound_order_id

    @inbound_order_id.setter
    def inbound_order_id(self, value):
        self._inbound_order_id = value
    @property
    def inbound_type(self):
        return self._inbound_type

    @inbound_type.setter
    def inbound_type(self, value):
        self._inbound_type = value
    @property
    def notice_date(self):
        return self._notice_date

    @notice_date.setter
    def notice_date(self, value):
        self._notice_date = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.inbound_order_id:
            if hasattr(self.inbound_order_id, 'to_alipay_dict'):
                params['inbound_order_id'] = self.inbound_order_id.to_alipay_dict()
            else:
                params['inbound_order_id'] = self.inbound_order_id
        if self.inbound_type:
            if hasattr(self.inbound_type, 'to_alipay_dict'):
                params['inbound_type'] = self.inbound_type.to_alipay_dict()
            else:
                params['inbound_type'] = self.inbound_type
        if self.notice_date:
            if hasattr(self.notice_date, 'to_alipay_dict'):
                params['notice_date'] = self.notice_date.to_alipay_dict()
            else:
                params['notice_date'] = self.notice_date
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.warehouse_code:
            if hasattr(self.warehouse_code, 'to_alipay_dict'):
                params['warehouse_code'] = self.warehouse_code.to_alipay_dict()
            else:
                params['warehouse_code'] = self.warehouse_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InboundOrderVO()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'inbound_order_id' in d:
            o.inbound_order_id = d['inbound_order_id']
        if 'inbound_type' in d:
            o.inbound_type = d['inbound_type']
        if 'notice_date' in d:
            o.notice_date = d['notice_date']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'status' in d:
            o.status = d['status']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        return o


