#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncInvoiceBatchqueryModel(object):

    def __init__(self):
        self._apply_order_id = None
        self._buyer_invoice_title = None
        self._buyer_ipid = None
        self._buyer_ipids = None
        self._buyer_iprole_id = None
        self._buyer_iprole_ids = None
        self._inst_id = None
        self._invoice_channel = None
        self._invoice_code = None
        self._invoice_create_date_begin = None
        self._invoice_create_date_end = None
        self._invoice_ids = None
        self._invoice_material = None
        self._invoice_no = None
        self._invoice_open_date_begin = None
        self._invoice_open_date_end = None
        self._invoice_status = None
        self._invoice_types = None
        self._is_online = None
        self._is_red = None
        self._mail_status = None
        self._monthly_bill_no = None
        self._page_no = None
        self._page_size = None
        self._tracking_no = None

    @property
    def apply_order_id(self):
        return self._apply_order_id

    @apply_order_id.setter
    def apply_order_id(self, value):
        self._apply_order_id = value
    @property
    def buyer_invoice_title(self):
        return self._buyer_invoice_title

    @buyer_invoice_title.setter
    def buyer_invoice_title(self, value):
        self._buyer_invoice_title = value
    @property
    def buyer_ipid(self):
        return self._buyer_ipid

    @buyer_ipid.setter
    def buyer_ipid(self, value):
        self._buyer_ipid = value
    @property
    def buyer_ipids(self):
        return self._buyer_ipids

    @buyer_ipids.setter
    def buyer_ipids(self, value):
        if isinstance(value, list):
            self._buyer_ipids = list()
            for i in value:
                self._buyer_ipids.append(i)
    @property
    def buyer_iprole_id(self):
        return self._buyer_iprole_id

    @buyer_iprole_id.setter
    def buyer_iprole_id(self, value):
        self._buyer_iprole_id = value
    @property
    def buyer_iprole_ids(self):
        return self._buyer_iprole_ids

    @buyer_iprole_ids.setter
    def buyer_iprole_ids(self, value):
        if isinstance(value, list):
            self._buyer_iprole_ids = list()
            for i in value:
                self._buyer_iprole_ids.append(i)
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def invoice_channel(self):
        return self._invoice_channel

    @invoice_channel.setter
    def invoice_channel(self, value):
        self._invoice_channel = value
    @property
    def invoice_code(self):
        return self._invoice_code

    @invoice_code.setter
    def invoice_code(self, value):
        self._invoice_code = value
    @property
    def invoice_create_date_begin(self):
        return self._invoice_create_date_begin

    @invoice_create_date_begin.setter
    def invoice_create_date_begin(self, value):
        self._invoice_create_date_begin = value
    @property
    def invoice_create_date_end(self):
        return self._invoice_create_date_end

    @invoice_create_date_end.setter
    def invoice_create_date_end(self, value):
        self._invoice_create_date_end = value
    @property
    def invoice_ids(self):
        return self._invoice_ids

    @invoice_ids.setter
    def invoice_ids(self, value):
        if isinstance(value, list):
            self._invoice_ids = list()
            for i in value:
                self._invoice_ids.append(i)
    @property
    def invoice_material(self):
        return self._invoice_material

    @invoice_material.setter
    def invoice_material(self, value):
        self._invoice_material = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_open_date_begin(self):
        return self._invoice_open_date_begin

    @invoice_open_date_begin.setter
    def invoice_open_date_begin(self, value):
        self._invoice_open_date_begin = value
    @property
    def invoice_open_date_end(self):
        return self._invoice_open_date_end

    @invoice_open_date_end.setter
    def invoice_open_date_end(self, value):
        self._invoice_open_date_end = value
    @property
    def invoice_status(self):
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        if isinstance(value, list):
            self._invoice_status = list()
            for i in value:
                self._invoice_status.append(i)
    @property
    def invoice_types(self):
        return self._invoice_types

    @invoice_types.setter
    def invoice_types(self, value):
        if isinstance(value, list):
            self._invoice_types = list()
            for i in value:
                self._invoice_types.append(i)
    @property
    def is_online(self):
        return self._is_online

    @is_online.setter
    def is_online(self, value):
        self._is_online = value
    @property
    def is_red(self):
        return self._is_red

    @is_red.setter
    def is_red(self, value):
        self._is_red = value
    @property
    def mail_status(self):
        return self._mail_status

    @mail_status.setter
    def mail_status(self, value):
        if isinstance(value, list):
            self._mail_status = list()
            for i in value:
                self._mail_status.append(i)
    @property
    def monthly_bill_no(self):
        return self._monthly_bill_no

    @monthly_bill_no.setter
    def monthly_bill_no(self, value):
        self._monthly_bill_no = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def tracking_no(self):
        return self._tracking_no

    @tracking_no.setter
    def tracking_no(self, value):
        self._tracking_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_order_id:
            if hasattr(self.apply_order_id, 'to_alipay_dict'):
                params['apply_order_id'] = self.apply_order_id.to_alipay_dict()
            else:
                params['apply_order_id'] = self.apply_order_id
        if self.buyer_invoice_title:
            if hasattr(self.buyer_invoice_title, 'to_alipay_dict'):
                params['buyer_invoice_title'] = self.buyer_invoice_title.to_alipay_dict()
            else:
                params['buyer_invoice_title'] = self.buyer_invoice_title
        if self.buyer_ipid:
            if hasattr(self.buyer_ipid, 'to_alipay_dict'):
                params['buyer_ipid'] = self.buyer_ipid.to_alipay_dict()
            else:
                params['buyer_ipid'] = self.buyer_ipid
        if self.buyer_ipids:
            if isinstance(self.buyer_ipids, list):
                for i in range(0, len(self.buyer_ipids)):
                    element = self.buyer_ipids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.buyer_ipids[i] = element.to_alipay_dict()
            if hasattr(self.buyer_ipids, 'to_alipay_dict'):
                params['buyer_ipids'] = self.buyer_ipids.to_alipay_dict()
            else:
                params['buyer_ipids'] = self.buyer_ipids
        if self.buyer_iprole_id:
            if hasattr(self.buyer_iprole_id, 'to_alipay_dict'):
                params['buyer_iprole_id'] = self.buyer_iprole_id.to_alipay_dict()
            else:
                params['buyer_iprole_id'] = self.buyer_iprole_id
        if self.buyer_iprole_ids:
            if isinstance(self.buyer_iprole_ids, list):
                for i in range(0, len(self.buyer_iprole_ids)):
                    element = self.buyer_iprole_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.buyer_iprole_ids[i] = element.to_alipay_dict()
            if hasattr(self.buyer_iprole_ids, 'to_alipay_dict'):
                params['buyer_iprole_ids'] = self.buyer_iprole_ids.to_alipay_dict()
            else:
                params['buyer_iprole_ids'] = self.buyer_iprole_ids
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.invoice_channel:
            if hasattr(self.invoice_channel, 'to_alipay_dict'):
                params['invoice_channel'] = self.invoice_channel.to_alipay_dict()
            else:
                params['invoice_channel'] = self.invoice_channel
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = self.invoice_code.to_alipay_dict()
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_create_date_begin:
            if hasattr(self.invoice_create_date_begin, 'to_alipay_dict'):
                params['invoice_create_date_begin'] = self.invoice_create_date_begin.to_alipay_dict()
            else:
                params['invoice_create_date_begin'] = self.invoice_create_date_begin
        if self.invoice_create_date_end:
            if hasattr(self.invoice_create_date_end, 'to_alipay_dict'):
                params['invoice_create_date_end'] = self.invoice_create_date_end.to_alipay_dict()
            else:
                params['invoice_create_date_end'] = self.invoice_create_date_end
        if self.invoice_ids:
            if isinstance(self.invoice_ids, list):
                for i in range(0, len(self.invoice_ids)):
                    element = self.invoice_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_ids[i] = element.to_alipay_dict()
            if hasattr(self.invoice_ids, 'to_alipay_dict'):
                params['invoice_ids'] = self.invoice_ids.to_alipay_dict()
            else:
                params['invoice_ids'] = self.invoice_ids
        if self.invoice_material:
            if hasattr(self.invoice_material, 'to_alipay_dict'):
                params['invoice_material'] = self.invoice_material.to_alipay_dict()
            else:
                params['invoice_material'] = self.invoice_material
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_open_date_begin:
            if hasattr(self.invoice_open_date_begin, 'to_alipay_dict'):
                params['invoice_open_date_begin'] = self.invoice_open_date_begin.to_alipay_dict()
            else:
                params['invoice_open_date_begin'] = self.invoice_open_date_begin
        if self.invoice_open_date_end:
            if hasattr(self.invoice_open_date_end, 'to_alipay_dict'):
                params['invoice_open_date_end'] = self.invoice_open_date_end.to_alipay_dict()
            else:
                params['invoice_open_date_end'] = self.invoice_open_date_end
        if self.invoice_status:
            if isinstance(self.invoice_status, list):
                for i in range(0, len(self.invoice_status)):
                    element = self.invoice_status[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_status[i] = element.to_alipay_dict()
            if hasattr(self.invoice_status, 'to_alipay_dict'):
                params['invoice_status'] = self.invoice_status.to_alipay_dict()
            else:
                params['invoice_status'] = self.invoice_status
        if self.invoice_types:
            if isinstance(self.invoice_types, list):
                for i in range(0, len(self.invoice_types)):
                    element = self.invoice_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_types[i] = element.to_alipay_dict()
            if hasattr(self.invoice_types, 'to_alipay_dict'):
                params['invoice_types'] = self.invoice_types.to_alipay_dict()
            else:
                params['invoice_types'] = self.invoice_types
        if self.is_online:
            if hasattr(self.is_online, 'to_alipay_dict'):
                params['is_online'] = self.is_online.to_alipay_dict()
            else:
                params['is_online'] = self.is_online
        if self.is_red:
            if hasattr(self.is_red, 'to_alipay_dict'):
                params['is_red'] = self.is_red.to_alipay_dict()
            else:
                params['is_red'] = self.is_red
        if self.mail_status:
            if isinstance(self.mail_status, list):
                for i in range(0, len(self.mail_status)):
                    element = self.mail_status[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mail_status[i] = element.to_alipay_dict()
            if hasattr(self.mail_status, 'to_alipay_dict'):
                params['mail_status'] = self.mail_status.to_alipay_dict()
            else:
                params['mail_status'] = self.mail_status
        if self.monthly_bill_no:
            if hasattr(self.monthly_bill_no, 'to_alipay_dict'):
                params['monthly_bill_no'] = self.monthly_bill_no.to_alipay_dict()
            else:
                params['monthly_bill_no'] = self.monthly_bill_no
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
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
        o = AlipayBossFncInvoiceBatchqueryModel()
        if 'apply_order_id' in d:
            o.apply_order_id = d['apply_order_id']
        if 'buyer_invoice_title' in d:
            o.buyer_invoice_title = d['buyer_invoice_title']
        if 'buyer_ipid' in d:
            o.buyer_ipid = d['buyer_ipid']
        if 'buyer_ipids' in d:
            o.buyer_ipids = d['buyer_ipids']
        if 'buyer_iprole_id' in d:
            o.buyer_iprole_id = d['buyer_iprole_id']
        if 'buyer_iprole_ids' in d:
            o.buyer_iprole_ids = d['buyer_iprole_ids']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'invoice_channel' in d:
            o.invoice_channel = d['invoice_channel']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_create_date_begin' in d:
            o.invoice_create_date_begin = d['invoice_create_date_begin']
        if 'invoice_create_date_end' in d:
            o.invoice_create_date_end = d['invoice_create_date_end']
        if 'invoice_ids' in d:
            o.invoice_ids = d['invoice_ids']
        if 'invoice_material' in d:
            o.invoice_material = d['invoice_material']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_open_date_begin' in d:
            o.invoice_open_date_begin = d['invoice_open_date_begin']
        if 'invoice_open_date_end' in d:
            o.invoice_open_date_end = d['invoice_open_date_end']
        if 'invoice_status' in d:
            o.invoice_status = d['invoice_status']
        if 'invoice_types' in d:
            o.invoice_types = d['invoice_types']
        if 'is_online' in d:
            o.is_online = d['is_online']
        if 'is_red' in d:
            o.is_red = d['is_red']
        if 'mail_status' in d:
            o.mail_status = d['mail_status']
        if 'monthly_bill_no' in d:
            o.monthly_bill_no = d['monthly_bill_no']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'tracking_no' in d:
            o.tracking_no = d['tracking_no']
        return o


