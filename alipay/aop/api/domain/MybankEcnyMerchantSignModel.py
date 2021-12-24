#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcnyAddressInfo import EcnyAddressInfo
from alipay.aop.api.domain.UserBaseInfo import UserBaseInfo
from alipay.aop.api.domain.UserBaseInfo import UserBaseInfo


class MybankEcnyMerchantSignModel(object):

    def __init__(self):
        self._agreement_type = None
        self._alipay_logon_id = None
        self._business_address = None
        self._cert_file = None
        self._cert_no = None
        self._cert_type = None
        self._concat_info = None
        self._ext_merchant_id = None
        self._in_door_images = None
        self._legal_rep_info = None
        self._mcc = None
        self._merchant_alias_name = None
        self._merchant_name = None
        self._merchant_type = None
        self._other_cert_files = None
        self._other_cert_type = None
        self._out_door_images = None
        self._out_request_no = None
        self._qualification_file = None
        self._qualification_type = None
        self._rate = None
        self._wallet_id = None

    @property
    def agreement_type(self):
        return self._agreement_type

    @agreement_type.setter
    def agreement_type(self, value):
        self._agreement_type = value
    @property
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
    @property
    def business_address(self):
        return self._business_address

    @business_address.setter
    def business_address(self, value):
        if isinstance(value, EcnyAddressInfo):
            self._business_address = value
        else:
            self._business_address = EcnyAddressInfo.from_alipay_dict(value)
    @property
    def cert_file(self):
        return self._cert_file

    @cert_file.setter
    def cert_file(self, value):
        self._cert_file = value
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
    def concat_info(self):
        return self._concat_info

    @concat_info.setter
    def concat_info(self, value):
        if isinstance(value, UserBaseInfo):
            self._concat_info = value
        else:
            self._concat_info = UserBaseInfo.from_alipay_dict(value)
    @property
    def ext_merchant_id(self):
        return self._ext_merchant_id

    @ext_merchant_id.setter
    def ext_merchant_id(self, value):
        self._ext_merchant_id = value
    @property
    def in_door_images(self):
        return self._in_door_images

    @in_door_images.setter
    def in_door_images(self, value):
        if isinstance(value, list):
            self._in_door_images = list()
            for i in value:
                self._in_door_images.append(i)
    @property
    def legal_rep_info(self):
        return self._legal_rep_info

    @legal_rep_info.setter
    def legal_rep_info(self, value):
        if isinstance(value, UserBaseInfo):
            self._legal_rep_info = value
        else:
            self._legal_rep_info = UserBaseInfo.from_alipay_dict(value)
    @property
    def mcc(self):
        return self._mcc

    @mcc.setter
    def mcc(self, value):
        self._mcc = value
    @property
    def merchant_alias_name(self):
        return self._merchant_alias_name

    @merchant_alias_name.setter
    def merchant_alias_name(self, value):
        self._merchant_alias_name = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_type(self):
        return self._merchant_type

    @merchant_type.setter
    def merchant_type(self, value):
        self._merchant_type = value
    @property
    def other_cert_files(self):
        return self._other_cert_files

    @other_cert_files.setter
    def other_cert_files(self, value):
        if isinstance(value, list):
            self._other_cert_files = list()
            for i in value:
                self._other_cert_files.append(i)
    @property
    def other_cert_type(self):
        return self._other_cert_type

    @other_cert_type.setter
    def other_cert_type(self, value):
        self._other_cert_type = value
    @property
    def out_door_images(self):
        return self._out_door_images

    @out_door_images.setter
    def out_door_images(self, value):
        if isinstance(value, list):
            self._out_door_images = list()
            for i in value:
                self._out_door_images.append(i)
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def qualification_file(self):
        return self._qualification_file

    @qualification_file.setter
    def qualification_file(self, value):
        self._qualification_file = value
    @property
    def qualification_type(self):
        return self._qualification_type

    @qualification_type.setter
    def qualification_type(self, value):
        self._qualification_type = value
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def wallet_id(self):
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, value):
        self._wallet_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_type:
            if hasattr(self.agreement_type, 'to_alipay_dict'):
                params['agreement_type'] = self.agreement_type.to_alipay_dict()
            else:
                params['agreement_type'] = self.agreement_type
        if self.alipay_logon_id:
            if hasattr(self.alipay_logon_id, 'to_alipay_dict'):
                params['alipay_logon_id'] = self.alipay_logon_id.to_alipay_dict()
            else:
                params['alipay_logon_id'] = self.alipay_logon_id
        if self.business_address:
            if hasattr(self.business_address, 'to_alipay_dict'):
                params['business_address'] = self.business_address.to_alipay_dict()
            else:
                params['business_address'] = self.business_address
        if self.cert_file:
            if hasattr(self.cert_file, 'to_alipay_dict'):
                params['cert_file'] = self.cert_file.to_alipay_dict()
            else:
                params['cert_file'] = self.cert_file
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
        if self.concat_info:
            if hasattr(self.concat_info, 'to_alipay_dict'):
                params['concat_info'] = self.concat_info.to_alipay_dict()
            else:
                params['concat_info'] = self.concat_info
        if self.ext_merchant_id:
            if hasattr(self.ext_merchant_id, 'to_alipay_dict'):
                params['ext_merchant_id'] = self.ext_merchant_id.to_alipay_dict()
            else:
                params['ext_merchant_id'] = self.ext_merchant_id
        if self.in_door_images:
            if isinstance(self.in_door_images, list):
                for i in range(0, len(self.in_door_images)):
                    element = self.in_door_images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.in_door_images[i] = element.to_alipay_dict()
            if hasattr(self.in_door_images, 'to_alipay_dict'):
                params['in_door_images'] = self.in_door_images.to_alipay_dict()
            else:
                params['in_door_images'] = self.in_door_images
        if self.legal_rep_info:
            if hasattr(self.legal_rep_info, 'to_alipay_dict'):
                params['legal_rep_info'] = self.legal_rep_info.to_alipay_dict()
            else:
                params['legal_rep_info'] = self.legal_rep_info
        if self.mcc:
            if hasattr(self.mcc, 'to_alipay_dict'):
                params['mcc'] = self.mcc.to_alipay_dict()
            else:
                params['mcc'] = self.mcc
        if self.merchant_alias_name:
            if hasattr(self.merchant_alias_name, 'to_alipay_dict'):
                params['merchant_alias_name'] = self.merchant_alias_name.to_alipay_dict()
            else:
                params['merchant_alias_name'] = self.merchant_alias_name
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.merchant_type:
            if hasattr(self.merchant_type, 'to_alipay_dict'):
                params['merchant_type'] = self.merchant_type.to_alipay_dict()
            else:
                params['merchant_type'] = self.merchant_type
        if self.other_cert_files:
            if isinstance(self.other_cert_files, list):
                for i in range(0, len(self.other_cert_files)):
                    element = self.other_cert_files[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_cert_files[i] = element.to_alipay_dict()
            if hasattr(self.other_cert_files, 'to_alipay_dict'):
                params['other_cert_files'] = self.other_cert_files.to_alipay_dict()
            else:
                params['other_cert_files'] = self.other_cert_files
        if self.other_cert_type:
            if hasattr(self.other_cert_type, 'to_alipay_dict'):
                params['other_cert_type'] = self.other_cert_type.to_alipay_dict()
            else:
                params['other_cert_type'] = self.other_cert_type
        if self.out_door_images:
            if isinstance(self.out_door_images, list):
                for i in range(0, len(self.out_door_images)):
                    element = self.out_door_images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_door_images[i] = element.to_alipay_dict()
            if hasattr(self.out_door_images, 'to_alipay_dict'):
                params['out_door_images'] = self.out_door_images.to_alipay_dict()
            else:
                params['out_door_images'] = self.out_door_images
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.qualification_file:
            if hasattr(self.qualification_file, 'to_alipay_dict'):
                params['qualification_file'] = self.qualification_file.to_alipay_dict()
            else:
                params['qualification_file'] = self.qualification_file
        if self.qualification_type:
            if hasattr(self.qualification_type, 'to_alipay_dict'):
                params['qualification_type'] = self.qualification_type.to_alipay_dict()
            else:
                params['qualification_type'] = self.qualification_type
        if self.rate:
            if hasattr(self.rate, 'to_alipay_dict'):
                params['rate'] = self.rate.to_alipay_dict()
            else:
                params['rate'] = self.rate
        if self.wallet_id:
            if hasattr(self.wallet_id, 'to_alipay_dict'):
                params['wallet_id'] = self.wallet_id.to_alipay_dict()
            else:
                params['wallet_id'] = self.wallet_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankEcnyMerchantSignModel()
        if 'agreement_type' in d:
            o.agreement_type = d['agreement_type']
        if 'alipay_logon_id' in d:
            o.alipay_logon_id = d['alipay_logon_id']
        if 'business_address' in d:
            o.business_address = d['business_address']
        if 'cert_file' in d:
            o.cert_file = d['cert_file']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'concat_info' in d:
            o.concat_info = d['concat_info']
        if 'ext_merchant_id' in d:
            o.ext_merchant_id = d['ext_merchant_id']
        if 'in_door_images' in d:
            o.in_door_images = d['in_door_images']
        if 'legal_rep_info' in d:
            o.legal_rep_info = d['legal_rep_info']
        if 'mcc' in d:
            o.mcc = d['mcc']
        if 'merchant_alias_name' in d:
            o.merchant_alias_name = d['merchant_alias_name']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'merchant_type' in d:
            o.merchant_type = d['merchant_type']
        if 'other_cert_files' in d:
            o.other_cert_files = d['other_cert_files']
        if 'other_cert_type' in d:
            o.other_cert_type = d['other_cert_type']
        if 'out_door_images' in d:
            o.out_door_images = d['out_door_images']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'qualification_file' in d:
            o.qualification_file = d['qualification_file']
        if 'qualification_type' in d:
            o.qualification_type = d['qualification_type']
        if 'rate' in d:
            o.rate = d['rate']
        if 'wallet_id' in d:
            o.wallet_id = d['wallet_id']
        return o


