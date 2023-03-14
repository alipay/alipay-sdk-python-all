#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntlcNdaProtocolSignRecordExtDO(object):

    def __init__(self):
        self._antlc_certificate_key = None
        self._expedite_status = None
        self._gmt_create = None
        self._gmt_modified = None
        self._id = None
        self._instl_id = None
        self._last_expedite_time = None
        self._sign_mode = None
        self._sign_status = None
        self._sign_time = None
        self._signator_2088 = None
        self._signator_corp_id = None
        self._signator_staff_id = None
        self._signator_staff_name = None
        self._signator_staff_union_id = None
        self._signed_file_addr = None
        self._tx_hash_code = None

    @property
    def antlc_certificate_key(self):
        return self._antlc_certificate_key

    @antlc_certificate_key.setter
    def antlc_certificate_key(self, value):
        self._antlc_certificate_key = value
    @property
    def expedite_status(self):
        return self._expedite_status

    @expedite_status.setter
    def expedite_status(self, value):
        self._expedite_status = value
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
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def instl_id(self):
        return self._instl_id

    @instl_id.setter
    def instl_id(self, value):
        self._instl_id = value
    @property
    def last_expedite_time(self):
        return self._last_expedite_time

    @last_expedite_time.setter
    def last_expedite_time(self, value):
        self._last_expedite_time = value
    @property
    def sign_mode(self):
        return self._sign_mode

    @sign_mode.setter
    def sign_mode(self, value):
        self._sign_mode = value
    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value
    @property
    def signator_2088(self):
        return self._signator_2088

    @signator_2088.setter
    def signator_2088(self, value):
        self._signator_2088 = value
    @property
    def signator_corp_id(self):
        return self._signator_corp_id

    @signator_corp_id.setter
    def signator_corp_id(self, value):
        self._signator_corp_id = value
    @property
    def signator_staff_id(self):
        return self._signator_staff_id

    @signator_staff_id.setter
    def signator_staff_id(self, value):
        self._signator_staff_id = value
    @property
    def signator_staff_name(self):
        return self._signator_staff_name

    @signator_staff_name.setter
    def signator_staff_name(self, value):
        self._signator_staff_name = value
    @property
    def signator_staff_union_id(self):
        return self._signator_staff_union_id

    @signator_staff_union_id.setter
    def signator_staff_union_id(self, value):
        self._signator_staff_union_id = value
    @property
    def signed_file_addr(self):
        return self._signed_file_addr

    @signed_file_addr.setter
    def signed_file_addr(self, value):
        self._signed_file_addr = value
    @property
    def tx_hash_code(self):
        return self._tx_hash_code

    @tx_hash_code.setter
    def tx_hash_code(self, value):
        self._tx_hash_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.antlc_certificate_key:
            if hasattr(self.antlc_certificate_key, 'to_alipay_dict'):
                params['antlc_certificate_key'] = self.antlc_certificate_key.to_alipay_dict()
            else:
                params['antlc_certificate_key'] = self.antlc_certificate_key
        if self.expedite_status:
            if hasattr(self.expedite_status, 'to_alipay_dict'):
                params['expedite_status'] = self.expedite_status.to_alipay_dict()
            else:
                params['expedite_status'] = self.expedite_status
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
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.instl_id:
            if hasattr(self.instl_id, 'to_alipay_dict'):
                params['instl_id'] = self.instl_id.to_alipay_dict()
            else:
                params['instl_id'] = self.instl_id
        if self.last_expedite_time:
            if hasattr(self.last_expedite_time, 'to_alipay_dict'):
                params['last_expedite_time'] = self.last_expedite_time.to_alipay_dict()
            else:
                params['last_expedite_time'] = self.last_expedite_time
        if self.sign_mode:
            if hasattr(self.sign_mode, 'to_alipay_dict'):
                params['sign_mode'] = self.sign_mode.to_alipay_dict()
            else:
                params['sign_mode'] = self.sign_mode
        if self.sign_status:
            if hasattr(self.sign_status, 'to_alipay_dict'):
                params['sign_status'] = self.sign_status.to_alipay_dict()
            else:
                params['sign_status'] = self.sign_status
        if self.sign_time:
            if hasattr(self.sign_time, 'to_alipay_dict'):
                params['sign_time'] = self.sign_time.to_alipay_dict()
            else:
                params['sign_time'] = self.sign_time
        if self.signator_2088:
            if hasattr(self.signator_2088, 'to_alipay_dict'):
                params['signator_2088'] = self.signator_2088.to_alipay_dict()
            else:
                params['signator_2088'] = self.signator_2088
        if self.signator_corp_id:
            if hasattr(self.signator_corp_id, 'to_alipay_dict'):
                params['signator_corp_id'] = self.signator_corp_id.to_alipay_dict()
            else:
                params['signator_corp_id'] = self.signator_corp_id
        if self.signator_staff_id:
            if hasattr(self.signator_staff_id, 'to_alipay_dict'):
                params['signator_staff_id'] = self.signator_staff_id.to_alipay_dict()
            else:
                params['signator_staff_id'] = self.signator_staff_id
        if self.signator_staff_name:
            if hasattr(self.signator_staff_name, 'to_alipay_dict'):
                params['signator_staff_name'] = self.signator_staff_name.to_alipay_dict()
            else:
                params['signator_staff_name'] = self.signator_staff_name
        if self.signator_staff_union_id:
            if hasattr(self.signator_staff_union_id, 'to_alipay_dict'):
                params['signator_staff_union_id'] = self.signator_staff_union_id.to_alipay_dict()
            else:
                params['signator_staff_union_id'] = self.signator_staff_union_id
        if self.signed_file_addr:
            if hasattr(self.signed_file_addr, 'to_alipay_dict'):
                params['signed_file_addr'] = self.signed_file_addr.to_alipay_dict()
            else:
                params['signed_file_addr'] = self.signed_file_addr
        if self.tx_hash_code:
            if hasattr(self.tx_hash_code, 'to_alipay_dict'):
                params['tx_hash_code'] = self.tx_hash_code.to_alipay_dict()
            else:
                params['tx_hash_code'] = self.tx_hash_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntlcNdaProtocolSignRecordExtDO()
        if 'antlc_certificate_key' in d:
            o.antlc_certificate_key = d['antlc_certificate_key']
        if 'expedite_status' in d:
            o.expedite_status = d['expedite_status']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'instl_id' in d:
            o.instl_id = d['instl_id']
        if 'last_expedite_time' in d:
            o.last_expedite_time = d['last_expedite_time']
        if 'sign_mode' in d:
            o.sign_mode = d['sign_mode']
        if 'sign_status' in d:
            o.sign_status = d['sign_status']
        if 'sign_time' in d:
            o.sign_time = d['sign_time']
        if 'signator_2088' in d:
            o.signator_2088 = d['signator_2088']
        if 'signator_corp_id' in d:
            o.signator_corp_id = d['signator_corp_id']
        if 'signator_staff_id' in d:
            o.signator_staff_id = d['signator_staff_id']
        if 'signator_staff_name' in d:
            o.signator_staff_name = d['signator_staff_name']
        if 'signator_staff_union_id' in d:
            o.signator_staff_union_id = d['signator_staff_union_id']
        if 'signed_file_addr' in d:
            o.signed_file_addr = d['signed_file_addr']
        if 'tx_hash_code' in d:
            o.tx_hash_code = d['tx_hash_code']
        return o


