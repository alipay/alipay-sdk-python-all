#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContactUserInfo import ContactUserInfo


class AlipayFundMbpcardPurchaseSignModel(object):

    def __init__(self):
        self._algorithm_name = None
        self._alipay_identity_id = None
        self._alipay_identity_type = None
        self._cert_image = None
        self._cert_image_back = None
        self._cert_no = None
        self._cert_type = None
        self._cipher_type = None
        self._contact_infos = None
        self._legal_cert_back_image = None
        self._legal_cert_front_image = None
        self._legal_cert_no = None
        self._legal_name = None
        self._legal_phone = None
        self._open_id = None
        self._out_request_no = None
        self._public_rsa_key = None
        self._user_name = None

    @property
    def algorithm_name(self):
        return self._algorithm_name

    @algorithm_name.setter
    def algorithm_name(self, value):
        self._algorithm_name = value
    @property
    def alipay_identity_id(self):
        return self._alipay_identity_id

    @alipay_identity_id.setter
    def alipay_identity_id(self, value):
        self._alipay_identity_id = value
    @property
    def alipay_identity_type(self):
        return self._alipay_identity_type

    @alipay_identity_type.setter
    def alipay_identity_type(self, value):
        self._alipay_identity_type = value
    @property
    def cert_image(self):
        return self._cert_image

    @cert_image.setter
    def cert_image(self, value):
        self._cert_image = value
    @property
    def cert_image_back(self):
        return self._cert_image_back

    @cert_image_back.setter
    def cert_image_back(self, value):
        self._cert_image_back = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def cipher_type(self):
        return self._cipher_type

    @cipher_type.setter
    def cipher_type(self, value):
        self._cipher_type = value
    @property
    def contact_infos(self):
        return self._contact_infos

    @contact_infos.setter
    def contact_infos(self, value):
        if isinstance(value, list):
            self._contact_infos = list()
            for i in value:
                if isinstance(i, ContactUserInfo):
                    self._contact_infos.append(i)
                else:
                    self._contact_infos.append(ContactUserInfo.from_alipay_dict(i))
    @property
    def legal_cert_back_image(self):
        return self._legal_cert_back_image

    @legal_cert_back_image.setter
    def legal_cert_back_image(self, value):
        self._legal_cert_back_image = value
    @property
    def legal_cert_front_image(self):
        return self._legal_cert_front_image

    @legal_cert_front_image.setter
    def legal_cert_front_image(self, value):
        self._legal_cert_front_image = value
    @property
    def legal_cert_no(self):
        return self._legal_cert_no

    @legal_cert_no.setter
    def legal_cert_no(self, value):
        self._legal_cert_no = value
    @property
    def legal_name(self):
        return self._legal_name

    @legal_name.setter
    def legal_name(self, value):
        self._legal_name = value
    @property
    def legal_phone(self):
        return self._legal_phone

    @legal_phone.setter
    def legal_phone(self, value):
        self._legal_phone = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def public_rsa_key(self):
        return self._public_rsa_key

    @public_rsa_key.setter
    def public_rsa_key(self, value):
        self._public_rsa_key = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.algorithm_name:
            if hasattr(self.algorithm_name, 'to_alipay_dict'):
                params['algorithm_name'] = self.algorithm_name.to_alipay_dict()
            else:
                params['algorithm_name'] = self.algorithm_name
        if self.alipay_identity_id:
            if hasattr(self.alipay_identity_id, 'to_alipay_dict'):
                params['alipay_identity_id'] = self.alipay_identity_id.to_alipay_dict()
            else:
                params['alipay_identity_id'] = self.alipay_identity_id
        if self.alipay_identity_type:
            if hasattr(self.alipay_identity_type, 'to_alipay_dict'):
                params['alipay_identity_type'] = self.alipay_identity_type.to_alipay_dict()
            else:
                params['alipay_identity_type'] = self.alipay_identity_type
        if self.cert_image:
            if hasattr(self.cert_image, 'to_alipay_dict'):
                params['cert_image'] = self.cert_image.to_alipay_dict()
            else:
                params['cert_image'] = self.cert_image
        if self.cert_image_back:
            if hasattr(self.cert_image_back, 'to_alipay_dict'):
                params['cert_image_back'] = self.cert_image_back.to_alipay_dict()
            else:
                params['cert_image_back'] = self.cert_image_back
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.cipher_type:
            if hasattr(self.cipher_type, 'to_alipay_dict'):
                params['cipher_type'] = self.cipher_type.to_alipay_dict()
            else:
                params['cipher_type'] = self.cipher_type
        if self.contact_infos:
            if isinstance(self.contact_infos, list):
                for i in range(0, len(self.contact_infos)):
                    element = self.contact_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contact_infos[i] = element.to_alipay_dict()
            if hasattr(self.contact_infos, 'to_alipay_dict'):
                params['contact_infos'] = self.contact_infos.to_alipay_dict()
            else:
                params['contact_infos'] = self.contact_infos
        if self.legal_cert_back_image:
            if hasattr(self.legal_cert_back_image, 'to_alipay_dict'):
                params['legal_cert_back_image'] = self.legal_cert_back_image.to_alipay_dict()
            else:
                params['legal_cert_back_image'] = self.legal_cert_back_image
        if self.legal_cert_front_image:
            if hasattr(self.legal_cert_front_image, 'to_alipay_dict'):
                params['legal_cert_front_image'] = self.legal_cert_front_image.to_alipay_dict()
            else:
                params['legal_cert_front_image'] = self.legal_cert_front_image
        if self.legal_cert_no:
            if hasattr(self.legal_cert_no, 'to_alipay_dict'):
                params['legal_cert_no'] = self.legal_cert_no.to_alipay_dict()
            else:
                params['legal_cert_no'] = self.legal_cert_no
        if self.legal_name:
            if hasattr(self.legal_name, 'to_alipay_dict'):
                params['legal_name'] = self.legal_name.to_alipay_dict()
            else:
                params['legal_name'] = self.legal_name
        if self.legal_phone:
            if hasattr(self.legal_phone, 'to_alipay_dict'):
                params['legal_phone'] = self.legal_phone.to_alipay_dict()
            else:
                params['legal_phone'] = self.legal_phone
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.public_rsa_key:
            if hasattr(self.public_rsa_key, 'to_alipay_dict'):
                params['public_rsa_key'] = self.public_rsa_key.to_alipay_dict()
            else:
                params['public_rsa_key'] = self.public_rsa_key
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundMbpcardPurchaseSignModel()
        if 'algorithm_name' in d:
            o.algorithm_name = d['algorithm_name']
        if 'alipay_identity_id' in d:
            o.alipay_identity_id = d['alipay_identity_id']
        if 'alipay_identity_type' in d:
            o.alipay_identity_type = d['alipay_identity_type']
        if 'cert_image' in d:
            o.cert_image = d['cert_image']
        if 'cert_image_back' in d:
            o.cert_image_back = d['cert_image_back']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'cipher_type' in d:
            o.cipher_type = d['cipher_type']
        if 'contact_infos' in d:
            o.contact_infos = d['contact_infos']
        if 'legal_cert_back_image' in d:
            o.legal_cert_back_image = d['legal_cert_back_image']
        if 'legal_cert_front_image' in d:
            o.legal_cert_front_image = d['legal_cert_front_image']
        if 'legal_cert_no' in d:
            o.legal_cert_no = d['legal_cert_no']
        if 'legal_name' in d:
            o.legal_name = d['legal_name']
        if 'legal_phone' in d:
            o.legal_phone = d['legal_phone']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'public_rsa_key' in d:
            o.public_rsa_key = d['public_rsa_key']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


