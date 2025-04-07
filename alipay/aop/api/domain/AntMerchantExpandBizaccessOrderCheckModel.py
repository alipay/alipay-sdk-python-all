#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CertificateInfoForEntry import CertificateInfoForEntry
from alipay.aop.api.domain.IsvCommissionInfo import IsvCommissionInfo
from alipay.aop.api.domain.CertificateInfoForEntry import CertificateInfoForEntry
from alipay.aop.api.domain.CommonMerchantLicenseInfo import CommonMerchantLicenseInfo
from alipay.aop.api.domain.MerchantPriceRelatedInfo import MerchantPriceRelatedInfo
from alipay.aop.api.domain.CommonMerchantLicenseInfo import CommonMerchantLicenseInfo


class AntMerchantExpandBizaccessOrderCheckModel(object):

    def __init__(self):
        self._benefit_info = None
        self._isv_commission_info = None
        self._legal_info = None
        self._legal_person_logon_id = None
        self._license_info = None
        self._mcc_code = None
        self._merchant_logon_id = None
        self._merchant_name = None
        self._merchant_type = None
        self._need_interface_auth = None
        self._need_operation_auth = None
        self._need_register_merchant = None
        self._optional_front_prod_code = None
        self._phone = None
        self._price_infos = None
        self._qualifications = None
        self._scene_biz_code = None

    @property
    def benefit_info(self):
        return self._benefit_info

    @benefit_info.setter
    def benefit_info(self, value):
        if isinstance(value, CertificateInfoForEntry):
            self._benefit_info = value
        else:
            self._benefit_info = CertificateInfoForEntry.from_alipay_dict(value)
    @property
    def isv_commission_info(self):
        return self._isv_commission_info

    @isv_commission_info.setter
    def isv_commission_info(self, value):
        if isinstance(value, list):
            self._isv_commission_info = list()
            for i in value:
                if isinstance(i, IsvCommissionInfo):
                    self._isv_commission_info.append(i)
                else:
                    self._isv_commission_info.append(IsvCommissionInfo.from_alipay_dict(i))
    @property
    def legal_info(self):
        return self._legal_info

    @legal_info.setter
    def legal_info(self, value):
        if isinstance(value, CertificateInfoForEntry):
            self._legal_info = value
        else:
            self._legal_info = CertificateInfoForEntry.from_alipay_dict(value)
    @property
    def legal_person_logon_id(self):
        return self._legal_person_logon_id

    @legal_person_logon_id.setter
    def legal_person_logon_id(self, value):
        self._legal_person_logon_id = value
    @property
    def license_info(self):
        return self._license_info

    @license_info.setter
    def license_info(self, value):
        if isinstance(value, CommonMerchantLicenseInfo):
            self._license_info = value
        else:
            self._license_info = CommonMerchantLicenseInfo.from_alipay_dict(value)
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def merchant_logon_id(self):
        return self._merchant_logon_id

    @merchant_logon_id.setter
    def merchant_logon_id(self, value):
        self._merchant_logon_id = value
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
    def need_interface_auth(self):
        return self._need_interface_auth

    @need_interface_auth.setter
    def need_interface_auth(self, value):
        self._need_interface_auth = value
    @property
    def need_operation_auth(self):
        return self._need_operation_auth

    @need_operation_auth.setter
    def need_operation_auth(self, value):
        self._need_operation_auth = value
    @property
    def need_register_merchant(self):
        return self._need_register_merchant

    @need_register_merchant.setter
    def need_register_merchant(self, value):
        self._need_register_merchant = value
    @property
    def optional_front_prod_code(self):
        return self._optional_front_prod_code

    @optional_front_prod_code.setter
    def optional_front_prod_code(self, value):
        if isinstance(value, list):
            self._optional_front_prod_code = list()
            for i in value:
                self._optional_front_prod_code.append(i)
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def price_infos(self):
        return self._price_infos

    @price_infos.setter
    def price_infos(self, value):
        if isinstance(value, list):
            self._price_infos = list()
            for i in value:
                if isinstance(i, MerchantPriceRelatedInfo):
                    self._price_infos.append(i)
                else:
                    self._price_infos.append(MerchantPriceRelatedInfo.from_alipay_dict(i))
    @property
    def qualifications(self):
        return self._qualifications

    @qualifications.setter
    def qualifications(self, value):
        if isinstance(value, list):
            self._qualifications = list()
            for i in value:
                if isinstance(i, CommonMerchantLicenseInfo):
                    self._qualifications.append(i)
                else:
                    self._qualifications.append(CommonMerchantLicenseInfo.from_alipay_dict(i))
    @property
    def scene_biz_code(self):
        return self._scene_biz_code

    @scene_biz_code.setter
    def scene_biz_code(self, value):
        if isinstance(value, list):
            self._scene_biz_code = list()
            for i in value:
                self._scene_biz_code.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_info:
            if hasattr(self.benefit_info, 'to_alipay_dict'):
                params['benefit_info'] = self.benefit_info.to_alipay_dict()
            else:
                params['benefit_info'] = self.benefit_info
        if self.isv_commission_info:
            if isinstance(self.isv_commission_info, list):
                for i in range(0, len(self.isv_commission_info)):
                    element = self.isv_commission_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.isv_commission_info[i] = element.to_alipay_dict()
            if hasattr(self.isv_commission_info, 'to_alipay_dict'):
                params['isv_commission_info'] = self.isv_commission_info.to_alipay_dict()
            else:
                params['isv_commission_info'] = self.isv_commission_info
        if self.legal_info:
            if hasattr(self.legal_info, 'to_alipay_dict'):
                params['legal_info'] = self.legal_info.to_alipay_dict()
            else:
                params['legal_info'] = self.legal_info
        if self.legal_person_logon_id:
            if hasattr(self.legal_person_logon_id, 'to_alipay_dict'):
                params['legal_person_logon_id'] = self.legal_person_logon_id.to_alipay_dict()
            else:
                params['legal_person_logon_id'] = self.legal_person_logon_id
        if self.license_info:
            if hasattr(self.license_info, 'to_alipay_dict'):
                params['license_info'] = self.license_info.to_alipay_dict()
            else:
                params['license_info'] = self.license_info
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = self.mcc_code.to_alipay_dict()
            else:
                params['mcc_code'] = self.mcc_code
        if self.merchant_logon_id:
            if hasattr(self.merchant_logon_id, 'to_alipay_dict'):
                params['merchant_logon_id'] = self.merchant_logon_id.to_alipay_dict()
            else:
                params['merchant_logon_id'] = self.merchant_logon_id
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
        if self.need_interface_auth:
            if hasattr(self.need_interface_auth, 'to_alipay_dict'):
                params['need_interface_auth'] = self.need_interface_auth.to_alipay_dict()
            else:
                params['need_interface_auth'] = self.need_interface_auth
        if self.need_operation_auth:
            if hasattr(self.need_operation_auth, 'to_alipay_dict'):
                params['need_operation_auth'] = self.need_operation_auth.to_alipay_dict()
            else:
                params['need_operation_auth'] = self.need_operation_auth
        if self.need_register_merchant:
            if hasattr(self.need_register_merchant, 'to_alipay_dict'):
                params['need_register_merchant'] = self.need_register_merchant.to_alipay_dict()
            else:
                params['need_register_merchant'] = self.need_register_merchant
        if self.optional_front_prod_code:
            if isinstance(self.optional_front_prod_code, list):
                for i in range(0, len(self.optional_front_prod_code)):
                    element = self.optional_front_prod_code[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.optional_front_prod_code[i] = element.to_alipay_dict()
            if hasattr(self.optional_front_prod_code, 'to_alipay_dict'):
                params['optional_front_prod_code'] = self.optional_front_prod_code.to_alipay_dict()
            else:
                params['optional_front_prod_code'] = self.optional_front_prod_code
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.price_infos:
            if isinstance(self.price_infos, list):
                for i in range(0, len(self.price_infos)):
                    element = self.price_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.price_infos[i] = element.to_alipay_dict()
            if hasattr(self.price_infos, 'to_alipay_dict'):
                params['price_infos'] = self.price_infos.to_alipay_dict()
            else:
                params['price_infos'] = self.price_infos
        if self.qualifications:
            if isinstance(self.qualifications, list):
                for i in range(0, len(self.qualifications)):
                    element = self.qualifications[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.qualifications[i] = element.to_alipay_dict()
            if hasattr(self.qualifications, 'to_alipay_dict'):
                params['qualifications'] = self.qualifications.to_alipay_dict()
            else:
                params['qualifications'] = self.qualifications
        if self.scene_biz_code:
            if isinstance(self.scene_biz_code, list):
                for i in range(0, len(self.scene_biz_code)):
                    element = self.scene_biz_code[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scene_biz_code[i] = element.to_alipay_dict()
            if hasattr(self.scene_biz_code, 'to_alipay_dict'):
                params['scene_biz_code'] = self.scene_biz_code.to_alipay_dict()
            else:
                params['scene_biz_code'] = self.scene_biz_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandBizaccessOrderCheckModel()
        if 'benefit_info' in d:
            o.benefit_info = d['benefit_info']
        if 'isv_commission_info' in d:
            o.isv_commission_info = d['isv_commission_info']
        if 'legal_info' in d:
            o.legal_info = d['legal_info']
        if 'legal_person_logon_id' in d:
            o.legal_person_logon_id = d['legal_person_logon_id']
        if 'license_info' in d:
            o.license_info = d['license_info']
        if 'mcc_code' in d:
            o.mcc_code = d['mcc_code']
        if 'merchant_logon_id' in d:
            o.merchant_logon_id = d['merchant_logon_id']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'merchant_type' in d:
            o.merchant_type = d['merchant_type']
        if 'need_interface_auth' in d:
            o.need_interface_auth = d['need_interface_auth']
        if 'need_operation_auth' in d:
            o.need_operation_auth = d['need_operation_auth']
        if 'need_register_merchant' in d:
            o.need_register_merchant = d['need_register_merchant']
        if 'optional_front_prod_code' in d:
            o.optional_front_prod_code = d['optional_front_prod_code']
        if 'phone' in d:
            o.phone = d['phone']
        if 'price_infos' in d:
            o.price_infos = d['price_infos']
        if 'qualifications' in d:
            o.qualifications = d['qualifications']
        if 'scene_biz_code' in d:
            o.scene_biz_code = d['scene_biz_code']
        return o


