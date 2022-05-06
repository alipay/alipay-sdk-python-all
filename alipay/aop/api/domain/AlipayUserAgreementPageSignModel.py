#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AccessParams import AccessParams
from alipay.aop.api.domain.DeviceParams import DeviceParams
from alipay.aop.api.domain.IdentityParams import IdentityParams
from alipay.aop.api.domain.PeriodRuleParams import PeriodRuleParams
from alipay.aop.api.domain.ProdParams import ProdParams
from alipay.aop.api.domain.SpecifiedAsset import SpecifiedAsset
from alipay.aop.api.domain.SpecifiedChannelParam import SpecifiedChannelParam
from alipay.aop.api.domain.SubMerchantParams import SubMerchantParams
from alipay.aop.api.domain.ZmAuthParams import ZmAuthParams


class AlipayUserAgreementPageSignModel(object):

    def __init__(self):
        self._access_params = None
        self._agreement_effect_type = None
        self._allow_huazhi_degrade = None
        self._device_params = None
        self._effect_time = None
        self._external_agreement_no = None
        self._external_logon_id = None
        self._identity_params = None
        self._merchant_process_url = None
        self._pass_params = None
        self._period_rule_params = None
        self._personal_product_code = None
        self._prod_params = None
        self._product_code = None
        self._promo_params = None
        self._sign_scene = None
        self._sign_validity_period = None
        self._specified_asset = None
        self._specified_sort_channel_params = None
        self._sub_merchant = None
        self._third_party_type = None
        self._user_age_range = None
        self._zm_auth_params = None

    @property
    def access_params(self):
        return self._access_params

    @access_params.setter
    def access_params(self, value):
        if isinstance(value, AccessParams):
            self._access_params = value
        else:
            self._access_params = AccessParams.from_alipay_dict(value)
    @property
    def agreement_effect_type(self):
        return self._agreement_effect_type

    @agreement_effect_type.setter
    def agreement_effect_type(self, value):
        self._agreement_effect_type = value
    @property
    def allow_huazhi_degrade(self):
        return self._allow_huazhi_degrade

    @allow_huazhi_degrade.setter
    def allow_huazhi_degrade(self, value):
        self._allow_huazhi_degrade = value
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
    def effect_time(self):
        return self._effect_time

    @effect_time.setter
    def effect_time(self, value):
        self._effect_time = value
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
    def identity_params(self):
        return self._identity_params

    @identity_params.setter
    def identity_params(self, value):
        if isinstance(value, IdentityParams):
            self._identity_params = value
        else:
            self._identity_params = IdentityParams.from_alipay_dict(value)
    @property
    def merchant_process_url(self):
        return self._merchant_process_url

    @merchant_process_url.setter
    def merchant_process_url(self, value):
        self._merchant_process_url = value
    @property
    def pass_params(self):
        return self._pass_params

    @pass_params.setter
    def pass_params(self, value):
        self._pass_params = value
    @property
    def period_rule_params(self):
        return self._period_rule_params

    @period_rule_params.setter
    def period_rule_params(self, value):
        if isinstance(value, PeriodRuleParams):
            self._period_rule_params = value
        else:
            self._period_rule_params = PeriodRuleParams.from_alipay_dict(value)
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
    def specified_asset(self):
        return self._specified_asset

    @specified_asset.setter
    def specified_asset(self, value):
        if isinstance(value, SpecifiedAsset):
            self._specified_asset = value
        else:
            self._specified_asset = SpecifiedAsset.from_alipay_dict(value)
    @property
    def specified_sort_channel_params(self):
        return self._specified_sort_channel_params

    @specified_sort_channel_params.setter
    def specified_sort_channel_params(self, value):
        if isinstance(value, SpecifiedChannelParam):
            self._specified_sort_channel_params = value
        else:
            self._specified_sort_channel_params = SpecifiedChannelParam.from_alipay_dict(value)
    @property
    def sub_merchant(self):
        return self._sub_merchant

    @sub_merchant.setter
    def sub_merchant(self, value):
        if isinstance(value, SubMerchantParams):
            self._sub_merchant = value
        else:
            self._sub_merchant = SubMerchantParams.from_alipay_dict(value)
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
        if self.access_params:
            if hasattr(self.access_params, 'to_alipay_dict'):
                params['access_params'] = self.access_params.to_alipay_dict()
            else:
                params['access_params'] = self.access_params
        if self.agreement_effect_type:
            if hasattr(self.agreement_effect_type, 'to_alipay_dict'):
                params['agreement_effect_type'] = self.agreement_effect_type.to_alipay_dict()
            else:
                params['agreement_effect_type'] = self.agreement_effect_type
        if self.allow_huazhi_degrade:
            if hasattr(self.allow_huazhi_degrade, 'to_alipay_dict'):
                params['allow_huazhi_degrade'] = self.allow_huazhi_degrade.to_alipay_dict()
            else:
                params['allow_huazhi_degrade'] = self.allow_huazhi_degrade
        if self.device_params:
            if hasattr(self.device_params, 'to_alipay_dict'):
                params['device_params'] = self.device_params.to_alipay_dict()
            else:
                params['device_params'] = self.device_params
        if self.effect_time:
            if hasattr(self.effect_time, 'to_alipay_dict'):
                params['effect_time'] = self.effect_time.to_alipay_dict()
            else:
                params['effect_time'] = self.effect_time
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
        if self.identity_params:
            if hasattr(self.identity_params, 'to_alipay_dict'):
                params['identity_params'] = self.identity_params.to_alipay_dict()
            else:
                params['identity_params'] = self.identity_params
        if self.merchant_process_url:
            if hasattr(self.merchant_process_url, 'to_alipay_dict'):
                params['merchant_process_url'] = self.merchant_process_url.to_alipay_dict()
            else:
                params['merchant_process_url'] = self.merchant_process_url
        if self.pass_params:
            if hasattr(self.pass_params, 'to_alipay_dict'):
                params['pass_params'] = self.pass_params.to_alipay_dict()
            else:
                params['pass_params'] = self.pass_params
        if self.period_rule_params:
            if hasattr(self.period_rule_params, 'to_alipay_dict'):
                params['period_rule_params'] = self.period_rule_params.to_alipay_dict()
            else:
                params['period_rule_params'] = self.period_rule_params
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
        if self.specified_asset:
            if hasattr(self.specified_asset, 'to_alipay_dict'):
                params['specified_asset'] = self.specified_asset.to_alipay_dict()
            else:
                params['specified_asset'] = self.specified_asset
        if self.specified_sort_channel_params:
            if hasattr(self.specified_sort_channel_params, 'to_alipay_dict'):
                params['specified_sort_channel_params'] = self.specified_sort_channel_params.to_alipay_dict()
            else:
                params['specified_sort_channel_params'] = self.specified_sort_channel_params
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
        o = AlipayUserAgreementPageSignModel()
        if 'access_params' in d:
            o.access_params = d['access_params']
        if 'agreement_effect_type' in d:
            o.agreement_effect_type = d['agreement_effect_type']
        if 'allow_huazhi_degrade' in d:
            o.allow_huazhi_degrade = d['allow_huazhi_degrade']
        if 'device_params' in d:
            o.device_params = d['device_params']
        if 'effect_time' in d:
            o.effect_time = d['effect_time']
        if 'external_agreement_no' in d:
            o.external_agreement_no = d['external_agreement_no']
        if 'external_logon_id' in d:
            o.external_logon_id = d['external_logon_id']
        if 'identity_params' in d:
            o.identity_params = d['identity_params']
        if 'merchant_process_url' in d:
            o.merchant_process_url = d['merchant_process_url']
        if 'pass_params' in d:
            o.pass_params = d['pass_params']
        if 'period_rule_params' in d:
            o.period_rule_params = d['period_rule_params']
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
        if 'specified_asset' in d:
            o.specified_asset = d['specified_asset']
        if 'specified_sort_channel_params' in d:
            o.specified_sort_channel_params = d['specified_sort_channel_params']
        if 'sub_merchant' in d:
            o.sub_merchant = d['sub_merchant']
        if 'third_party_type' in d:
            o.third_party_type = d['third_party_type']
        if 'user_age_range' in d:
            o.user_age_range = d['user_age_range']
        if 'zm_auth_params' in d:
            o.zm_auth_params = d['zm_auth_params']
        return o


