#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainIdentityInfoCertifyModel(object):

    def __init__(self):
        self._alipay_uid = None
        self._biz_code = None
        self._biz_id = None
        self._certify_enum = None
        self._channel = None
        self._ep_cert_name = None
        self._ep_cert_no = None
        self._ep_cert_no_type = None
        self._l_person_cert_name = None
        self._l_person_cert_no = None
        self._l_person_certno_type = None
        self._owner_name = None
        self._owner_uid = None
        self._person_cert_no = None
        self._person_cert_type = None
        self._person_name = None

    @property
    def alipay_uid(self):
        return self._alipay_uid

    @alipay_uid.setter
    def alipay_uid(self, value):
        self._alipay_uid = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def certify_enum(self):
        return self._certify_enum

    @certify_enum.setter
    def certify_enum(self, value):
        self._certify_enum = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def ep_cert_name(self):
        return self._ep_cert_name

    @ep_cert_name.setter
    def ep_cert_name(self, value):
        self._ep_cert_name = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_cert_no_type(self):
        return self._ep_cert_no_type

    @ep_cert_no_type.setter
    def ep_cert_no_type(self, value):
        self._ep_cert_no_type = value
    @property
    def l_person_cert_name(self):
        return self._l_person_cert_name

    @l_person_cert_name.setter
    def l_person_cert_name(self, value):
        self._l_person_cert_name = value
    @property
    def l_person_cert_no(self):
        return self._l_person_cert_no

    @l_person_cert_no.setter
    def l_person_cert_no(self, value):
        self._l_person_cert_no = value
    @property
    def l_person_certno_type(self):
        return self._l_person_certno_type

    @l_person_certno_type.setter
    def l_person_certno_type(self, value):
        self._l_person_certno_type = value
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value
    @property
    def owner_uid(self):
        return self._owner_uid

    @owner_uid.setter
    def owner_uid(self, value):
        self._owner_uid = value
    @property
    def person_cert_no(self):
        return self._person_cert_no

    @person_cert_no.setter
    def person_cert_no(self, value):
        self._person_cert_no = value
    @property
    def person_cert_type(self):
        return self._person_cert_type

    @person_cert_type.setter
    def person_cert_type(self, value):
        self._person_cert_type = value
    @property
    def person_name(self):
        return self._person_name

    @person_name.setter
    def person_name(self, value):
        self._person_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_uid:
            if hasattr(self.alipay_uid, 'to_alipay_dict'):
                params['alipay_uid'] = self.alipay_uid.to_alipay_dict()
            else:
                params['alipay_uid'] = self.alipay_uid
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.certify_enum:
            if hasattr(self.certify_enum, 'to_alipay_dict'):
                params['certify_enum'] = self.certify_enum.to_alipay_dict()
            else:
                params['certify_enum'] = self.certify_enum
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.ep_cert_name:
            if hasattr(self.ep_cert_name, 'to_alipay_dict'):
                params['ep_cert_name'] = self.ep_cert_name.to_alipay_dict()
            else:
                params['ep_cert_name'] = self.ep_cert_name
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.ep_cert_no_type:
            if hasattr(self.ep_cert_no_type, 'to_alipay_dict'):
                params['ep_cert_no_type'] = self.ep_cert_no_type.to_alipay_dict()
            else:
                params['ep_cert_no_type'] = self.ep_cert_no_type
        if self.l_person_cert_name:
            if hasattr(self.l_person_cert_name, 'to_alipay_dict'):
                params['l_person_cert_name'] = self.l_person_cert_name.to_alipay_dict()
            else:
                params['l_person_cert_name'] = self.l_person_cert_name
        if self.l_person_cert_no:
            if hasattr(self.l_person_cert_no, 'to_alipay_dict'):
                params['l_person_cert_no'] = self.l_person_cert_no.to_alipay_dict()
            else:
                params['l_person_cert_no'] = self.l_person_cert_no
        if self.l_person_certno_type:
            if hasattr(self.l_person_certno_type, 'to_alipay_dict'):
                params['l_person_certno_type'] = self.l_person_certno_type.to_alipay_dict()
            else:
                params['l_person_certno_type'] = self.l_person_certno_type
        if self.owner_name:
            if hasattr(self.owner_name, 'to_alipay_dict'):
                params['owner_name'] = self.owner_name.to_alipay_dict()
            else:
                params['owner_name'] = self.owner_name
        if self.owner_uid:
            if hasattr(self.owner_uid, 'to_alipay_dict'):
                params['owner_uid'] = self.owner_uid.to_alipay_dict()
            else:
                params['owner_uid'] = self.owner_uid
        if self.person_cert_no:
            if hasattr(self.person_cert_no, 'to_alipay_dict'):
                params['person_cert_no'] = self.person_cert_no.to_alipay_dict()
            else:
                params['person_cert_no'] = self.person_cert_no
        if self.person_cert_type:
            if hasattr(self.person_cert_type, 'to_alipay_dict'):
                params['person_cert_type'] = self.person_cert_type.to_alipay_dict()
            else:
                params['person_cert_type'] = self.person_cert_type
        if self.person_name:
            if hasattr(self.person_name, 'to_alipay_dict'):
                params['person_name'] = self.person_name.to_alipay_dict()
            else:
                params['person_name'] = self.person_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainIdentityInfoCertifyModel()
        if 'alipay_uid' in d:
            o.alipay_uid = d['alipay_uid']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'certify_enum' in d:
            o.certify_enum = d['certify_enum']
        if 'channel' in d:
            o.channel = d['channel']
        if 'ep_cert_name' in d:
            o.ep_cert_name = d['ep_cert_name']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_cert_no_type' in d:
            o.ep_cert_no_type = d['ep_cert_no_type']
        if 'l_person_cert_name' in d:
            o.l_person_cert_name = d['l_person_cert_name']
        if 'l_person_cert_no' in d:
            o.l_person_cert_no = d['l_person_cert_no']
        if 'l_person_certno_type' in d:
            o.l_person_certno_type = d['l_person_certno_type']
        if 'owner_name' in d:
            o.owner_name = d['owner_name']
        if 'owner_uid' in d:
            o.owner_uid = d['owner_uid']
        if 'person_cert_no' in d:
            o.person_cert_no = d['person_cert_no']
        if 'person_cert_type' in d:
            o.person_cert_type = d['person_cert_type']
        if 'person_name' in d:
            o.person_name = d['person_name']
        return o


