#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsCertificateApiDTO(object):

    def __init__(self):
        self._biz_data = None
        self._certificate_no = None
        self._certificate_type = None
        self._effect_time = None
        self._expire_time = None
        self._face_value = None
        self._ins_policy_no = None
        self._inst_id = None
        self._order_id = None
        self._order_source = None
        self._out_biz_no = None
        self._owner_uid = None
        self._status = None
        self._use_time = None
        self._user_uid = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
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
    def effect_time(self):
        return self._effect_time

    @effect_time.setter
    def effect_time(self, value):
        self._effect_time = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def face_value(self):
        return self._face_value

    @face_value.setter
    def face_value(self, value):
        self._face_value = value
    @property
    def ins_policy_no(self):
        return self._ins_policy_no

    @ins_policy_no.setter
    def ins_policy_no(self, value):
        self._ins_policy_no = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def use_time(self):
        return self._use_time

    @use_time.setter
    def use_time(self, value):
        self._use_time = value
    @property
    def user_uid(self):
        return self._user_uid

    @user_uid.setter
    def user_uid(self, value):
        self._user_uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
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
        if self.effect_time:
            if hasattr(self.effect_time, 'to_alipay_dict'):
                params['effect_time'] = self.effect_time.to_alipay_dict()
            else:
                params['effect_time'] = self.effect_time
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.face_value:
            if hasattr(self.face_value, 'to_alipay_dict'):
                params['face_value'] = self.face_value.to_alipay_dict()
            else:
                params['face_value'] = self.face_value
        if self.ins_policy_no:
            if hasattr(self.ins_policy_no, 'to_alipay_dict'):
                params['ins_policy_no'] = self.ins_policy_no.to_alipay_dict()
            else:
                params['ins_policy_no'] = self.ins_policy_no
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.use_time:
            if hasattr(self.use_time, 'to_alipay_dict'):
                params['use_time'] = self.use_time.to_alipay_dict()
            else:
                params['use_time'] = self.use_time
        if self.user_uid:
            if hasattr(self.user_uid, 'to_alipay_dict'):
                params['user_uid'] = self.user_uid.to_alipay_dict()
            else:
                params['user_uid'] = self.user_uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsCertificateApiDTO()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'certificate_no' in d:
            o.certificate_no = d['certificate_no']
        if 'certificate_type' in d:
            o.certificate_type = d['certificate_type']
        if 'effect_time' in d:
            o.effect_time = d['effect_time']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'face_value' in d:
            o.face_value = d['face_value']
        if 'ins_policy_no' in d:
            o.ins_policy_no = d['ins_policy_no']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_source' in d:
            o.order_source = d['order_source']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'owner_uid' in d:
            o.owner_uid = d['owner_uid']
        if 'status' in d:
            o.status = d['status']
        if 'use_time' in d:
            o.use_time = d['use_time']
        if 'user_uid' in d:
            o.user_uid = d['user_uid']
        return o


