#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StandardVoucherVO(object):

    def __init__(self):
        self._event_code = None
        self._ext_info = None
        self._fund_biz_code = None
        self._fund_biz_name = None
        self._id = None
        self._idempotent_id = None
        self._out_biz_no = None
        self._prod_code = None
        self._trans_direction = None
        self._trans_inst_id = None
        self._voucher_type = None

    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def fund_biz_code(self):
        return self._fund_biz_code

    @fund_biz_code.setter
    def fund_biz_code(self, value):
        self._fund_biz_code = value
    @property
    def fund_biz_name(self):
        return self._fund_biz_name

    @fund_biz_name.setter
    def fund_biz_name(self, value):
        self._fund_biz_name = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def idempotent_id(self):
        return self._idempotent_id

    @idempotent_id.setter
    def idempotent_id(self, value):
        self._idempotent_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def trans_direction(self):
        return self._trans_direction

    @trans_direction.setter
    def trans_direction(self, value):
        self._trans_direction = value
    @property
    def trans_inst_id(self):
        return self._trans_inst_id

    @trans_inst_id.setter
    def trans_inst_id(self, value):
        self._trans_inst_id = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.fund_biz_code:
            if hasattr(self.fund_biz_code, 'to_alipay_dict'):
                params['fund_biz_code'] = self.fund_biz_code.to_alipay_dict()
            else:
                params['fund_biz_code'] = self.fund_biz_code
        if self.fund_biz_name:
            if hasattr(self.fund_biz_name, 'to_alipay_dict'):
                params['fund_biz_name'] = self.fund_biz_name.to_alipay_dict()
            else:
                params['fund_biz_name'] = self.fund_biz_name
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.idempotent_id:
            if hasattr(self.idempotent_id, 'to_alipay_dict'):
                params['idempotent_id'] = self.idempotent_id.to_alipay_dict()
            else:
                params['idempotent_id'] = self.idempotent_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.trans_direction:
            if hasattr(self.trans_direction, 'to_alipay_dict'):
                params['trans_direction'] = self.trans_direction.to_alipay_dict()
            else:
                params['trans_direction'] = self.trans_direction
        if self.trans_inst_id:
            if hasattr(self.trans_inst_id, 'to_alipay_dict'):
                params['trans_inst_id'] = self.trans_inst_id.to_alipay_dict()
            else:
                params['trans_inst_id'] = self.trans_inst_id
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StandardVoucherVO()
        if 'event_code' in d:
            o.event_code = d['event_code']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'fund_biz_code' in d:
            o.fund_biz_code = d['fund_biz_code']
        if 'fund_biz_name' in d:
            o.fund_biz_name = d['fund_biz_name']
        if 'id' in d:
            o.id = d['id']
        if 'idempotent_id' in d:
            o.idempotent_id = d['idempotent_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'trans_direction' in d:
            o.trans_direction = d['trans_direction']
        if 'trans_inst_id' in d:
            o.trans_inst_id = d['trans_inst_id']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


