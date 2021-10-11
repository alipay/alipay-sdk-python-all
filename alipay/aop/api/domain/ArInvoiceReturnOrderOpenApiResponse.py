#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ArInvoiceReturnOrderDetailOpenApiResponse import ArInvoiceReturnOrderDetailOpenApiResponse


class ArInvoiceReturnOrderOpenApiResponse(object):

    def __init__(self):
        self._ar_invoice_return_order_details = None
        self._creator = None
        self._gmt_create = None
        self._gmt_modified = None
        self._inst_id = None
        self._ip_id = None
        self._ip_role_id = None
        self._last_moder = None
        self._memo = None
        self._modified_item = None
        self._order_channel = None
        self._order_no = None
        self._order_status = None
        self._order_type = None
        self._process_instance_id = None
        self._re_invoice = None
        self._reject_reason = None
        self._return_reason_type = None
        self._tracking_no = None

    @property
    def ar_invoice_return_order_details(self):
        return self._ar_invoice_return_order_details

    @ar_invoice_return_order_details.setter
    def ar_invoice_return_order_details(self, value):
        if isinstance(value, list):
            self._ar_invoice_return_order_details = list()
            for i in value:
                if isinstance(i, ArInvoiceReturnOrderDetailOpenApiResponse):
                    self._ar_invoice_return_order_details.append(i)
                else:
                    self._ar_invoice_return_order_details.append(ArInvoiceReturnOrderDetailOpenApiResponse.from_alipay_dict(i))
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
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
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def last_moder(self):
        return self._last_moder

    @last_moder.setter
    def last_moder(self, value):
        self._last_moder = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def modified_item(self):
        return self._modified_item

    @modified_item.setter
    def modified_item(self, value):
        self._modified_item = value
    @property
    def order_channel(self):
        return self._order_channel

    @order_channel.setter
    def order_channel(self, value):
        self._order_channel = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
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
    def process_instance_id(self):
        return self._process_instance_id

    @process_instance_id.setter
    def process_instance_id(self, value):
        self._process_instance_id = value
    @property
    def re_invoice(self):
        return self._re_invoice

    @re_invoice.setter
    def re_invoice(self, value):
        self._re_invoice = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def return_reason_type(self):
        return self._return_reason_type

    @return_reason_type.setter
    def return_reason_type(self, value):
        self._return_reason_type = value
    @property
    def tracking_no(self):
        return self._tracking_no

    @tracking_no.setter
    def tracking_no(self, value):
        self._tracking_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ar_invoice_return_order_details:
            if isinstance(self.ar_invoice_return_order_details, list):
                for i in range(0, len(self.ar_invoice_return_order_details)):
                    element = self.ar_invoice_return_order_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ar_invoice_return_order_details[i] = element.to_alipay_dict()
            if hasattr(self.ar_invoice_return_order_details, 'to_alipay_dict'):
                params['ar_invoice_return_order_details'] = self.ar_invoice_return_order_details.to_alipay_dict()
            else:
                params['ar_invoice_return_order_details'] = self.ar_invoice_return_order_details
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
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
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.last_moder:
            if hasattr(self.last_moder, 'to_alipay_dict'):
                params['last_moder'] = self.last_moder.to_alipay_dict()
            else:
                params['last_moder'] = self.last_moder
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.modified_item:
            if hasattr(self.modified_item, 'to_alipay_dict'):
                params['modified_item'] = self.modified_item.to_alipay_dict()
            else:
                params['modified_item'] = self.modified_item
        if self.order_channel:
            if hasattr(self.order_channel, 'to_alipay_dict'):
                params['order_channel'] = self.order_channel.to_alipay_dict()
            else:
                params['order_channel'] = self.order_channel
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
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
        if self.process_instance_id:
            if hasattr(self.process_instance_id, 'to_alipay_dict'):
                params['process_instance_id'] = self.process_instance_id.to_alipay_dict()
            else:
                params['process_instance_id'] = self.process_instance_id
        if self.re_invoice:
            if hasattr(self.re_invoice, 'to_alipay_dict'):
                params['re_invoice'] = self.re_invoice.to_alipay_dict()
            else:
                params['re_invoice'] = self.re_invoice
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        if self.return_reason_type:
            if hasattr(self.return_reason_type, 'to_alipay_dict'):
                params['return_reason_type'] = self.return_reason_type.to_alipay_dict()
            else:
                params['return_reason_type'] = self.return_reason_type
        if self.tracking_no:
            if hasattr(self.tracking_no, 'to_alipay_dict'):
                params['tracking_no'] = self.tracking_no.to_alipay_dict()
            else:
                params['tracking_no'] = self.tracking_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArInvoiceReturnOrderOpenApiResponse()
        if 'ar_invoice_return_order_details' in d:
            o.ar_invoice_return_order_details = d['ar_invoice_return_order_details']
        if 'creator' in d:
            o.creator = d['creator']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'last_moder' in d:
            o.last_moder = d['last_moder']
        if 'memo' in d:
            o.memo = d['memo']
        if 'modified_item' in d:
            o.modified_item = d['modified_item']
        if 'order_channel' in d:
            o.order_channel = d['order_channel']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'process_instance_id' in d:
            o.process_instance_id = d['process_instance_id']
        if 're_invoice' in d:
            o.re_invoice = d['re_invoice']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        if 'return_reason_type' in d:
            o.return_reason_type = d['return_reason_type']
        if 'tracking_no' in d:
            o.tracking_no = d['tracking_no']
        return o


