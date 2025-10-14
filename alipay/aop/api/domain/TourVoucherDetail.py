#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TourVoucherDetail(object):

    def __init__(self):
        self._cert_no = None
        self._code_info = None
        self._identity_type = None
        self._name = None
        self._out_vercher_id = None
        self._out_voucher_id = None
        self._scenic_id = None
        self._source_num = None
        self._status = None
        self._tele_no = None
        self._verify_open_id = None
        self._verify_user_id = None
        self._voucher_info = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def code_info(self):
        return self._code_info

    @code_info.setter
    def code_info(self, value):
        self._code_info = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_vercher_id(self):
        return self._out_vercher_id

    @out_vercher_id.setter
    def out_vercher_id(self, value):
        self._out_vercher_id = value
    @property
    def out_voucher_id(self):
        return self._out_voucher_id

    @out_voucher_id.setter
    def out_voucher_id(self, value):
        self._out_voucher_id = value
    @property
    def scenic_id(self):
        return self._scenic_id

    @scenic_id.setter
    def scenic_id(self, value):
        self._scenic_id = value
    @property
    def source_num(self):
        return self._source_num

    @source_num.setter
    def source_num(self, value):
        self._source_num = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tele_no(self):
        return self._tele_no

    @tele_no.setter
    def tele_no(self, value):
        self._tele_no = value
    @property
    def verify_open_id(self):
        return self._verify_open_id

    @verify_open_id.setter
    def verify_open_id(self, value):
        self._verify_open_id = value
    @property
    def verify_user_id(self):
        return self._verify_user_id

    @verify_user_id.setter
    def verify_user_id(self, value):
        self._verify_user_id = value
    @property
    def voucher_info(self):
        return self._voucher_info

    @voucher_info.setter
    def voucher_info(self, value):
        self._voucher_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.code_info:
            if hasattr(self.code_info, 'to_alipay_dict'):
                params['code_info'] = self.code_info.to_alipay_dict()
            else:
                params['code_info'] = self.code_info
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_vercher_id:
            if hasattr(self.out_vercher_id, 'to_alipay_dict'):
                params['out_vercher_id'] = self.out_vercher_id.to_alipay_dict()
            else:
                params['out_vercher_id'] = self.out_vercher_id
        if self.out_voucher_id:
            if hasattr(self.out_voucher_id, 'to_alipay_dict'):
                params['out_voucher_id'] = self.out_voucher_id.to_alipay_dict()
            else:
                params['out_voucher_id'] = self.out_voucher_id
        if self.scenic_id:
            if hasattr(self.scenic_id, 'to_alipay_dict'):
                params['scenic_id'] = self.scenic_id.to_alipay_dict()
            else:
                params['scenic_id'] = self.scenic_id
        if self.source_num:
            if hasattr(self.source_num, 'to_alipay_dict'):
                params['source_num'] = self.source_num.to_alipay_dict()
            else:
                params['source_num'] = self.source_num
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tele_no:
            if hasattr(self.tele_no, 'to_alipay_dict'):
                params['tele_no'] = self.tele_no.to_alipay_dict()
            else:
                params['tele_no'] = self.tele_no
        if self.verify_open_id:
            if hasattr(self.verify_open_id, 'to_alipay_dict'):
                params['verify_open_id'] = self.verify_open_id.to_alipay_dict()
            else:
                params['verify_open_id'] = self.verify_open_id
        if self.verify_user_id:
            if hasattr(self.verify_user_id, 'to_alipay_dict'):
                params['verify_user_id'] = self.verify_user_id.to_alipay_dict()
            else:
                params['verify_user_id'] = self.verify_user_id
        if self.voucher_info:
            if hasattr(self.voucher_info, 'to_alipay_dict'):
                params['voucher_info'] = self.voucher_info.to_alipay_dict()
            else:
                params['voucher_info'] = self.voucher_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TourVoucherDetail()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'code_info' in d:
            o.code_info = d['code_info']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'name' in d:
            o.name = d['name']
        if 'out_vercher_id' in d:
            o.out_vercher_id = d['out_vercher_id']
        if 'out_voucher_id' in d:
            o.out_voucher_id = d['out_voucher_id']
        if 'scenic_id' in d:
            o.scenic_id = d['scenic_id']
        if 'source_num' in d:
            o.source_num = d['source_num']
        if 'status' in d:
            o.status = d['status']
        if 'tele_no' in d:
            o.tele_no = d['tele_no']
        if 'verify_open_id' in d:
            o.verify_open_id = d['verify_open_id']
        if 'verify_user_id' in d:
            o.verify_user_id = d['verify_user_id']
        if 'voucher_info' in d:
            o.voucher_info = d['voucher_info']
        return o


