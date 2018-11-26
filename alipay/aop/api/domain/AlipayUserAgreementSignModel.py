#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetParams import AssetParams
from alipay.aop.api.domain.DeviceParams import DeviceParams
from alipay.aop.api.domain.ProdParams import ProdParams
from alipay.aop.api.domain.VerifyParams import VerifyParams
from alipay.aop.api.domain.ZmAuthParams import ZmAuthParams


class AlipayUserAgreementSignModel(object):

    def __init__(self):
        self._alipay_logon_id = None
        self._alipay_user_id = None
        self._asset_params = None
        self._binded_mobile = None
        self._confirm_type = None
        self._device_params = None
        self._external_agreement_no = None
        self._external_logon_id = None
        self._personal_product_code = None
        self._prod_params = None
        self._product_code = None
        self._promo_params = None
        self._sign_scene = None
        self._sign_validity_period = None
        self._sub_merchant = None
        self._third_party_type = None
        self._user_age_range = None
        self._verify_params = None
        self._zm_auth_params = None

    @property
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def asset_params(self):
        return self._asset_params

    @asset_params.setter
    def asset_params(self, value):
        if isinstance(value, AssetParams):
            self._asset_params = value
        else:
            self._asset_params = AssetParams.from_alipay_dict(value)
    @property
    def binded_mobile(self):
        return self._binded_mobile

    @binded_mobile.setter
    def binded_mobile(self, value):
        self._binded_mobile = value
    @property
    def confirm_type(self):
        return self._confirm_type

    @confirm_type.setter
    def confirm_type(self, value):
        self._confirm_type = value
    @property
    def device_params(self):
        return self._device_params

    @device_params.setter
    def device_params(self, value):
        if isinstance(value, DeviceParams):
            self._device_params = value
        else:
            self._device_params = DeviceParams.from_alipay_dict(value)
    @property
    def external_agreement_no(self):
        return self._external_agreement_no

    @external_agreement_no.setter
    def external_agreement_no(self, value):
        self._external_agreement_no = value
    @property
    def external_logon_id(self):
        return self._external_logon_id

    @external_logon_id.setter
    def external_logon_id(self, value):
        self._external_logon_id = value
    @property
    def personal_product_code(self):
        return self._personal_product_code

    @personal_product_code.setter
    def personal_product_code(self, value):
        self._personal_product_code = value
    @property
    def prod_params(self):
        return self._prod_params

    @prod_params.setter
    def prod_params(self, value):
        if isinstance(value, ProdParams):
            self._prod_params = value
        else:
            self._prod_params = ProdParams.from_alipay_dict(value)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def promo_params(self):
        return self._promo_params

    @promo_params.setter
    def promo_params(self, value):
        self._promo_params = value
    @property
    def sign_scene(self):
        return self._sign_scene

    @sign_scene.setter
    def sign_scene(self, value):
        self._sign_scene = value
    @property
    def sign_validity_period(self):
        return self._sign_validity_period

    @sign_validity_period.setter
    def sign_validity_period(self, value):
        self._sign_validity_period = value
    @property
    def sub_merchant(self):
        return self._sub_merchant

    @sub_merchant.setter
    def sub_merchant(self, value):
        self._sub_merchant = value
    @property
    def third_party_type(self):
        return self._third_party_type

    @third_party_type.setter
    def third_party_type(self, value):
        self._third_party_type = value
    @property
    def user_age_range(self):
        return self._user_age_range

    @user_age_range.setter
    def user_age_range(self, value):
        self._user_age_range = value
    @property
    def verify_params(self):
        return self._verify_params

    @verify_params.setter
    def verify_params(self, value):
        if isinstance(value, VerifyParams):
            self._verify_params = value
        else:
            self._verify_params = VerifyParams.from_alipay_dict(value)
    @property
    def zm_auth_params(self):
        return self._zm_auth_params

    @zm_auth_params.setter
    def zm_auth_params(self, value):
        if isinstance(value, ZmAuthParams):
            self._zm_auth_params = value
        else:
            self._zm_auth_params = ZmAuthParams.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_logon_id:
            if hasattr(self.alipay_logon_id, 'to_alipay_dict'):
                params['alipay_logon_id'] = self.alipay_logon_id.to_alipay_dict()
            else:
                params['alipay_logon_id'] = self.alipay_logon_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.asset_params:
            if hasattr(self.asset_params, 'to_alipay_dict'):
                params['asset_params'] = self.asset_params.to_alipay_dict()
            else:
                params['asset_params'] = self.asset_params
        if self.binded_mobile:
            if hasattr(self.binded_mobile, 'to_alipay_dict'):
                params['binded_mobile'] = self.binded_mobile.to_alipay_dict()
            else:
                params['binded_mobile'] = self.binded_mobile
        if self.confirm_type:
            if hasattr(self.confirm_type, 'to_alipay_dict'):
                params['confirm_type'] = self.confirm_type.to_alipay_dict()
            else:
                params['confirm_type'] = self.confirm_type
        if self.device_params:
            if hasattr(self.device_params, 'to_alipay_dict'):
                params['device_params'] = self.device_params.to_alipay_dict()
            else:
                params['device_params'] = self.device_params
        if self.external_agreement_no:
            if hasattr(self.external_agreement_no, 'to_alipay_dict'):
                params['external_agreement_no'] = self.external_agreement_no.to_alipay_dict()
            else:
                params['external_agreement_no'] = self.external_agreement_no
        if self.external_logon_id:
            if hasattr(self.external_logon_id, 'to_alipay_dict'):
                params['external_logon_id'] = self.external_logon_id.to_alipay_dict()
            else:
                params['external_logon_id'] = self.external_logon_id
        if self.personal_product_code:
            if hasattr(self.personal_product_code, 'to_alipay_dict'):
                params['personal_product_code'] = self.personal_product_code.to_alipay_dict()
            else:
                params['personal_product_code'] = self.personal_product_code
        if self.prod_params:
            if hasattr(self.prod_params, 'to_alipay_dict'):
                params['prod_params'] = self.prod_params.to_alipay_dict()
            else:
                params['prod_params'] = self.prod_params
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.promo_params:
            if hasattr(self.promo_params, 'to_alipay_dict'):
                params['promo_params'] = self.promo_params.to_alipay_dict()
            else:
                params['promo_params'] = self.promo_params
        if self.sign_scene:
            if hasattr(self.sign_scene, 'to_alipay_dict'):
                params['sign_scene'] = self.sign_scene.to_alipay_dict()
            else:
                params['sign_scene'] = self.sign_scene
        if self.sign_validity_period:
            if hasattr(self.sign_validity_period, 'to_alipay_dict'):
                params['sign_validity_period'] = self.sign_validity_period.to_alipay_dict()
            else:
                params['sign_validity_period'] = self.sign_validity_period
        if self.sub_merchant:
            if hasattr(self.sub_merchant, 'to_alipay_dict'):
                params['sub_merchant'] = self.sub_merchant.to_alipay_dict()
            else:
                params['sub_merchant'] = self.sub_merchant
        if self.third_party_type:
            if hasattr(self.third_party_type, 'to_alipay_dict'):
                params['third_party_type'] = self.third_party_type.to_alipay_dict()
            else:
                params['third_party_type'] = self.third_party_type
        if self.user_age_range:
            if hasattr(self.user_age_range, 'to_alipay_dict'):
                params['user_age_range'] = self.user_age_range.to_alipay_dict()
            else:
                params['user_age_range'] = self.user_age_range
        if self.verify_params:
            if hasattr(self.verify_params, 'to_alipay_dict'):
                params['verify_params'] = self.verify_params.to_alipay_dict()
            else:
                params['verify_params'] = self.verify_params
        if self.zm_auth_params:
            if hasattr(self.zm_auth_params, 'to_alipay_dict'):
                params['zm_auth_params'] = self.zm_auth_params.to_alipay_dict()
            else:
                params['zm_auth_params'] = self.zm_auth_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAgreementSignModel()
        if 'alipay_logon_id' in d:
            o.alipay_logon_id = d['alipay_logon_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'asset_params' in d:
            o.asset_params = d['asset_params']
        if 'binded_mobile' in d:
            o.binded_mobile = d['binded_mobile']
        if 'confirm_type' in d:
            o.confirm_type = d['confirm_type']
        if 'device_params' in d:
            o.device_params = d['device_params']
        if 'external_agreement_no' in d:
            o.external_agreement_no = d['external_agreement_no']
        if 'external_logon_id' in d:
            o.external_logon_id = d['external_logon_id']
        if 'personal_product_code' in d:
            o.personal_product_code = d['personal_product_code']
        if 'prod_params' in d:
            o.prod_params = d['prod_params']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'promo_params' in d:
            o.promo_params = d['promo_params']
        if 'sign_scene' in d:
            o.sign_scene = d['sign_scene']
        if 'sign_validity_period' in d:
            o.sign_validity_period = d['sign_validity_period']
        if 'sub_merchant' in d:
            o.sub_merchant = d['sub_merchant']
        if 'third_party_type' in d:
            o.third_party_type = d['third_party_type']
        if 'user_age_range' in d:
            o.user_age_range = d['user_age_range']
        if 'verify_params' in d:
            o.verify_params = d['verify_params']
        if 'zm_auth_params' in d:
            o.zm_auth_params = d['zm_auth_params']
        return o


