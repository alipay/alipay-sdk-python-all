#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BankCardInfo import BankCardInfo


class AntMerchantExpandIndirectActivityCreateModel(object):

    def __init__(self):
        self._activity_type = None
        self._alias_name = None
        self._bank_account = None
        self._business_license_pic = None
        self._certificate_file = None
        self._charge_sample = None
        self._checkstand_pic = None
        self._diplomatic_note = None
        self._indoor_pic = None
        self._institutional_organization_pic = None
        self._legal_person_pic = None
        self._legal_person_registration_pic = None
        self._medical_instrument_practice_license_pic = None
        self._name = None
        self._org_cert_pic = None
        self._private_nonenterprise_units = None
        self._run_school_license_pic = None
        self._settled_pic = None
        self._shop_entrance_pic = None
        self._sub_merchant_id = None

    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def alias_name(self):
        return self._alias_name

    @alias_name.setter
    def alias_name(self, value):
        self._alias_name = value
    @property
    def bank_account(self):
        return self._bank_account

    @bank_account.setter
    def bank_account(self, value):
        if isinstance(value, BankCardInfo):
            self._bank_account = value
        else:
            self._bank_account = BankCardInfo.from_alipay_dict(value)
    @property
    def business_license_pic(self):
        return self._business_license_pic

    @business_license_pic.setter
    def business_license_pic(self, value):
        self._business_license_pic = value
    @property
    def certificate_file(self):
        return self._certificate_file

    @certificate_file.setter
    def certificate_file(self, value):
        self._certificate_file = value
    @property
    def charge_sample(self):
        return self._charge_sample

    @charge_sample.setter
    def charge_sample(self, value):
        self._charge_sample = value
    @property
    def checkstand_pic(self):
        return self._checkstand_pic

    @checkstand_pic.setter
    def checkstand_pic(self, value):
        self._checkstand_pic = value
    @property
    def diplomatic_note(self):
        return self._diplomatic_note

    @diplomatic_note.setter
    def diplomatic_note(self, value):
        self._diplomatic_note = value
    @property
    def indoor_pic(self):
        return self._indoor_pic

    @indoor_pic.setter
    def indoor_pic(self, value):
        self._indoor_pic = value
    @property
    def institutional_organization_pic(self):
        return self._institutional_organization_pic

    @institutional_organization_pic.setter
    def institutional_organization_pic(self, value):
        self._institutional_organization_pic = value
    @property
    def legal_person_pic(self):
        return self._legal_person_pic

    @legal_person_pic.setter
    def legal_person_pic(self, value):
        self._legal_person_pic = value
    @property
    def legal_person_registration_pic(self):
        return self._legal_person_registration_pic

    @legal_person_registration_pic.setter
    def legal_person_registration_pic(self, value):
        self._legal_person_registration_pic = value
    @property
    def medical_instrument_practice_license_pic(self):
        return self._medical_instrument_practice_license_pic

    @medical_instrument_practice_license_pic.setter
    def medical_instrument_practice_license_pic(self, value):
        self._medical_instrument_practice_license_pic = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def org_cert_pic(self):
        return self._org_cert_pic

    @org_cert_pic.setter
    def org_cert_pic(self, value):
        self._org_cert_pic = value
    @property
    def private_nonenterprise_units(self):
        return self._private_nonenterprise_units

    @private_nonenterprise_units.setter
    def private_nonenterprise_units(self, value):
        self._private_nonenterprise_units = value
    @property
    def run_school_license_pic(self):
        return self._run_school_license_pic

    @run_school_license_pic.setter
    def run_school_license_pic(self, value):
        self._run_school_license_pic = value
    @property
    def settled_pic(self):
        return self._settled_pic

    @settled_pic.setter
    def settled_pic(self, value):
        self._settled_pic = value
    @property
    def shop_entrance_pic(self):
        return self._shop_entrance_pic

    @shop_entrance_pic.setter
    def shop_entrance_pic(self, value):
        self._shop_entrance_pic = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.alias_name:
            if hasattr(self.alias_name, 'to_alipay_dict'):
                params['alias_name'] = self.alias_name.to_alipay_dict()
            else:
                params['alias_name'] = self.alias_name
        if self.bank_account:
            if hasattr(self.bank_account, 'to_alipay_dict'):
                params['bank_account'] = self.bank_account.to_alipay_dict()
            else:
                params['bank_account'] = self.bank_account
        if self.business_license_pic:
            if hasattr(self.business_license_pic, 'to_alipay_dict'):
                params['business_license_pic'] = self.business_license_pic.to_alipay_dict()
            else:
                params['business_license_pic'] = self.business_license_pic
        if self.certificate_file:
            if hasattr(self.certificate_file, 'to_alipay_dict'):
                params['certificate_file'] = self.certificate_file.to_alipay_dict()
            else:
                params['certificate_file'] = self.certificate_file
        if self.charge_sample:
            if hasattr(self.charge_sample, 'to_alipay_dict'):
                params['charge_sample'] = self.charge_sample.to_alipay_dict()
            else:
                params['charge_sample'] = self.charge_sample
        if self.checkstand_pic:
            if hasattr(self.checkstand_pic, 'to_alipay_dict'):
                params['checkstand_pic'] = self.checkstand_pic.to_alipay_dict()
            else:
                params['checkstand_pic'] = self.checkstand_pic
        if self.diplomatic_note:
            if hasattr(self.diplomatic_note, 'to_alipay_dict'):
                params['diplomatic_note'] = self.diplomatic_note.to_alipay_dict()
            else:
                params['diplomatic_note'] = self.diplomatic_note
        if self.indoor_pic:
            if hasattr(self.indoor_pic, 'to_alipay_dict'):
                params['indoor_pic'] = self.indoor_pic.to_alipay_dict()
            else:
                params['indoor_pic'] = self.indoor_pic
        if self.institutional_organization_pic:
            if hasattr(self.institutional_organization_pic, 'to_alipay_dict'):
                params['institutional_organization_pic'] = self.institutional_organization_pic.to_alipay_dict()
            else:
                params['institutional_organization_pic'] = self.institutional_organization_pic
        if self.legal_person_pic:
            if hasattr(self.legal_person_pic, 'to_alipay_dict'):
                params['legal_person_pic'] = self.legal_person_pic.to_alipay_dict()
            else:
                params['legal_person_pic'] = self.legal_person_pic
        if self.legal_person_registration_pic:
            if hasattr(self.legal_person_registration_pic, 'to_alipay_dict'):
                params['legal_person_registration_pic'] = self.legal_person_registration_pic.to_alipay_dict()
            else:
                params['legal_person_registration_pic'] = self.legal_person_registration_pic
        if self.medical_instrument_practice_license_pic:
            if hasattr(self.medical_instrument_practice_license_pic, 'to_alipay_dict'):
                params['medical_instrument_practice_license_pic'] = self.medical_instrument_practice_license_pic.to_alipay_dict()
            else:
                params['medical_instrument_practice_license_pic'] = self.medical_instrument_practice_license_pic
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.org_cert_pic:
            if hasattr(self.org_cert_pic, 'to_alipay_dict'):
                params['org_cert_pic'] = self.org_cert_pic.to_alipay_dict()
            else:
                params['org_cert_pic'] = self.org_cert_pic
        if self.private_nonenterprise_units:
            if hasattr(self.private_nonenterprise_units, 'to_alipay_dict'):
                params['private_nonenterprise_units'] = self.private_nonenterprise_units.to_alipay_dict()
            else:
                params['private_nonenterprise_units'] = self.private_nonenterprise_units
        if self.run_school_license_pic:
            if hasattr(self.run_school_license_pic, 'to_alipay_dict'):
                params['run_school_license_pic'] = self.run_school_license_pic.to_alipay_dict()
            else:
                params['run_school_license_pic'] = self.run_school_license_pic
        if self.settled_pic:
            if hasattr(self.settled_pic, 'to_alipay_dict'):
                params['settled_pic'] = self.settled_pic.to_alipay_dict()
            else:
                params['settled_pic'] = self.settled_pic
        if self.shop_entrance_pic:
            if hasattr(self.shop_entrance_pic, 'to_alipay_dict'):
                params['shop_entrance_pic'] = self.shop_entrance_pic.to_alipay_dict()
            else:
                params['shop_entrance_pic'] = self.shop_entrance_pic
        if self.sub_merchant_id:
            if hasattr(self.sub_merchant_id, 'to_alipay_dict'):
                params['sub_merchant_id'] = self.sub_merchant_id.to_alipay_dict()
            else:
                params['sub_merchant_id'] = self.sub_merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIndirectActivityCreateModel()
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'alias_name' in d:
            o.alias_name = d['alias_name']
        if 'bank_account' in d:
            o.bank_account = d['bank_account']
        if 'business_license_pic' in d:
            o.business_license_pic = d['business_license_pic']
        if 'certificate_file' in d:
            o.certificate_file = d['certificate_file']
        if 'charge_sample' in d:
            o.charge_sample = d['charge_sample']
        if 'checkstand_pic' in d:
            o.checkstand_pic = d['checkstand_pic']
        if 'diplomatic_note' in d:
            o.diplomatic_note = d['diplomatic_note']
        if 'indoor_pic' in d:
            o.indoor_pic = d['indoor_pic']
        if 'institutional_organization_pic' in d:
            o.institutional_organization_pic = d['institutional_organization_pic']
        if 'legal_person_pic' in d:
            o.legal_person_pic = d['legal_person_pic']
        if 'legal_person_registration_pic' in d:
            o.legal_person_registration_pic = d['legal_person_registration_pic']
        if 'medical_instrument_practice_license_pic' in d:
            o.medical_instrument_practice_license_pic = d['medical_instrument_practice_license_pic']
        if 'name' in d:
            o.name = d['name']
        if 'org_cert_pic' in d:
            o.org_cert_pic = d['org_cert_pic']
        if 'private_nonenterprise_units' in d:
            o.private_nonenterprise_units = d['private_nonenterprise_units']
        if 'run_school_license_pic' in d:
            o.run_school_license_pic = d['run_school_license_pic']
        if 'settled_pic' in d:
            o.settled_pic = d['settled_pic']
        if 'shop_entrance_pic' in d:
            o.shop_entrance_pic = d['shop_entrance_pic']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        return o


