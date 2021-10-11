#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BankCardInfo import BankCardInfo


class AntMerchantExpandIndirectActivityCreateModel(object):

    def __init__(self):
        self._activity_type = None
        self._alias_name = None
        self._app_market = None
        self._app_name = None
        self._app_screenshot = None
        self._app_status = None
        self._auth_license = None
        self._bank_account = None
        self._bank_account_prove = None
        self._bank_cooperation_agreement = None
        self._business_license_pic = None
        self._certificate_file = None
        self._charge_sample = None
        self._checkstand_pic = None
        self._diplomatic_note = None
        self._icp_license = None
        self._indoor_pic = None
        self._industry_code = None
        self._industry_qualification_image = None
        self._institutional_organization_pic = None
        self._legal_person_license_auth_pic = None
        self._legal_person_pic = None
        self._legal_person_registration_pic = None
        self._medical_instrument_practice_license_pic = None
        self._name = None
        self._org_cert_pic = None
        self._pc_site = None
        self._pc_site_status = None
        self._private_nonenterprise_units = None
        self._quota_per_day = None
        self._quota_per_each = None
        self._run_school_license_pic = None
        self._settled_pic = None
        self._shop_entrance_pic = None
        self._sub_merchant_id = None
        self._withhold_service_desc = None
        self._withhold_service_name = None

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
    def app_market(self):
        return self._app_market

    @app_market.setter
    def app_market(self, value):
        self._app_market = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_screenshot(self):
        return self._app_screenshot

    @app_screenshot.setter
    def app_screenshot(self, value):
        self._app_screenshot = value
    @property
    def app_status(self):
        return self._app_status

    @app_status.setter
    def app_status(self, value):
        self._app_status = value
    @property
    def auth_license(self):
        return self._auth_license

    @auth_license.setter
    def auth_license(self, value):
        self._auth_license = value
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
    def bank_account_prove(self):
        return self._bank_account_prove

    @bank_account_prove.setter
    def bank_account_prove(self, value):
        self._bank_account_prove = value
    @property
    def bank_cooperation_agreement(self):
        return self._bank_cooperation_agreement

    @bank_cooperation_agreement.setter
    def bank_cooperation_agreement(self, value):
        self._bank_cooperation_agreement = value
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
    def icp_license(self):
        return self._icp_license

    @icp_license.setter
    def icp_license(self, value):
        self._icp_license = value
    @property
    def indoor_pic(self):
        return self._indoor_pic

    @indoor_pic.setter
    def indoor_pic(self, value):
        self._indoor_pic = value
    @property
    def industry_code(self):
        return self._industry_code

    @industry_code.setter
    def industry_code(self, value):
        self._industry_code = value
    @property
    def industry_qualification_image(self):
        return self._industry_qualification_image

    @industry_qualification_image.setter
    def industry_qualification_image(self, value):
        self._industry_qualification_image = value
    @property
    def institutional_organization_pic(self):
        return self._institutional_organization_pic

    @institutional_organization_pic.setter
    def institutional_organization_pic(self, value):
        self._institutional_organization_pic = value
    @property
    def legal_person_license_auth_pic(self):
        return self._legal_person_license_auth_pic

    @legal_person_license_auth_pic.setter
    def legal_person_license_auth_pic(self, value):
        self._legal_person_license_auth_pic = value
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
    def pc_site(self):
        return self._pc_site

    @pc_site.setter
    def pc_site(self, value):
        self._pc_site = value
    @property
    def pc_site_status(self):
        return self._pc_site_status

    @pc_site_status.setter
    def pc_site_status(self, value):
        self._pc_site_status = value
    @property
    def private_nonenterprise_units(self):
        return self._private_nonenterprise_units

    @private_nonenterprise_units.setter
    def private_nonenterprise_units(self, value):
        self._private_nonenterprise_units = value
    @property
    def quota_per_day(self):
        return self._quota_per_day

    @quota_per_day.setter
    def quota_per_day(self, value):
        self._quota_per_day = value
    @property
    def quota_per_each(self):
        return self._quota_per_each

    @quota_per_each.setter
    def quota_per_each(self, value):
        self._quota_per_each = value
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
    @property
    def withhold_service_desc(self):
        return self._withhold_service_desc

    @withhold_service_desc.setter
    def withhold_service_desc(self, value):
        self._withhold_service_desc = value
    @property
    def withhold_service_name(self):
        return self._withhold_service_name

    @withhold_service_name.setter
    def withhold_service_name(self, value):
        self._withhold_service_name = value


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
        if self.app_market:
            if hasattr(self.app_market, 'to_alipay_dict'):
                params['app_market'] = self.app_market.to_alipay_dict()
            else:
                params['app_market'] = self.app_market
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_screenshot:
            if hasattr(self.app_screenshot, 'to_alipay_dict'):
                params['app_screenshot'] = self.app_screenshot.to_alipay_dict()
            else:
                params['app_screenshot'] = self.app_screenshot
        if self.app_status:
            if hasattr(self.app_status, 'to_alipay_dict'):
                params['app_status'] = self.app_status.to_alipay_dict()
            else:
                params['app_status'] = self.app_status
        if self.auth_license:
            if hasattr(self.auth_license, 'to_alipay_dict'):
                params['auth_license'] = self.auth_license.to_alipay_dict()
            else:
                params['auth_license'] = self.auth_license
        if self.bank_account:
            if hasattr(self.bank_account, 'to_alipay_dict'):
                params['bank_account'] = self.bank_account.to_alipay_dict()
            else:
                params['bank_account'] = self.bank_account
        if self.bank_account_prove:
            if hasattr(self.bank_account_prove, 'to_alipay_dict'):
                params['bank_account_prove'] = self.bank_account_prove.to_alipay_dict()
            else:
                params['bank_account_prove'] = self.bank_account_prove
        if self.bank_cooperation_agreement:
            if hasattr(self.bank_cooperation_agreement, 'to_alipay_dict'):
                params['bank_cooperation_agreement'] = self.bank_cooperation_agreement.to_alipay_dict()
            else:
                params['bank_cooperation_agreement'] = self.bank_cooperation_agreement
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
        if self.icp_license:
            if hasattr(self.icp_license, 'to_alipay_dict'):
                params['icp_license'] = self.icp_license.to_alipay_dict()
            else:
                params['icp_license'] = self.icp_license
        if self.indoor_pic:
            if hasattr(self.indoor_pic, 'to_alipay_dict'):
                params['indoor_pic'] = self.indoor_pic.to_alipay_dict()
            else:
                params['indoor_pic'] = self.indoor_pic
        if self.industry_code:
            if hasattr(self.industry_code, 'to_alipay_dict'):
                params['industry_code'] = self.industry_code.to_alipay_dict()
            else:
                params['industry_code'] = self.industry_code
        if self.industry_qualification_image:
            if hasattr(self.industry_qualification_image, 'to_alipay_dict'):
                params['industry_qualification_image'] = self.industry_qualification_image.to_alipay_dict()
            else:
                params['industry_qualification_image'] = self.industry_qualification_image
        if self.institutional_organization_pic:
            if hasattr(self.institutional_organization_pic, 'to_alipay_dict'):
                params['institutional_organization_pic'] = self.institutional_organization_pic.to_alipay_dict()
            else:
                params['institutional_organization_pic'] = self.institutional_organization_pic
        if self.legal_person_license_auth_pic:
            if hasattr(self.legal_person_license_auth_pic, 'to_alipay_dict'):
                params['legal_person_license_auth_pic'] = self.legal_person_license_auth_pic.to_alipay_dict()
            else:
                params['legal_person_license_auth_pic'] = self.legal_person_license_auth_pic
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
        if self.pc_site:
            if hasattr(self.pc_site, 'to_alipay_dict'):
                params['pc_site'] = self.pc_site.to_alipay_dict()
            else:
                params['pc_site'] = self.pc_site
        if self.pc_site_status:
            if hasattr(self.pc_site_status, 'to_alipay_dict'):
                params['pc_site_status'] = self.pc_site_status.to_alipay_dict()
            else:
                params['pc_site_status'] = self.pc_site_status
        if self.private_nonenterprise_units:
            if hasattr(self.private_nonenterprise_units, 'to_alipay_dict'):
                params['private_nonenterprise_units'] = self.private_nonenterprise_units.to_alipay_dict()
            else:
                params['private_nonenterprise_units'] = self.private_nonenterprise_units
        if self.quota_per_day:
            if hasattr(self.quota_per_day, 'to_alipay_dict'):
                params['quota_per_day'] = self.quota_per_day.to_alipay_dict()
            else:
                params['quota_per_day'] = self.quota_per_day
        if self.quota_per_each:
            if hasattr(self.quota_per_each, 'to_alipay_dict'):
                params['quota_per_each'] = self.quota_per_each.to_alipay_dict()
            else:
                params['quota_per_each'] = self.quota_per_each
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
        if self.withhold_service_desc:
            if hasattr(self.withhold_service_desc, 'to_alipay_dict'):
                params['withhold_service_desc'] = self.withhold_service_desc.to_alipay_dict()
            else:
                params['withhold_service_desc'] = self.withhold_service_desc
        if self.withhold_service_name:
            if hasattr(self.withhold_service_name, 'to_alipay_dict'):
                params['withhold_service_name'] = self.withhold_service_name.to_alipay_dict()
            else:
                params['withhold_service_name'] = self.withhold_service_name
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
        if 'app_market' in d:
            o.app_market = d['app_market']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_screenshot' in d:
            o.app_screenshot = d['app_screenshot']
        if 'app_status' in d:
            o.app_status = d['app_status']
        if 'auth_license' in d:
            o.auth_license = d['auth_license']
        if 'bank_account' in d:
            o.bank_account = d['bank_account']
        if 'bank_account_prove' in d:
            o.bank_account_prove = d['bank_account_prove']
        if 'bank_cooperation_agreement' in d:
            o.bank_cooperation_agreement = d['bank_cooperation_agreement']
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
        if 'icp_license' in d:
            o.icp_license = d['icp_license']
        if 'indoor_pic' in d:
            o.indoor_pic = d['indoor_pic']
        if 'industry_code' in d:
            o.industry_code = d['industry_code']
        if 'industry_qualification_image' in d:
            o.industry_qualification_image = d['industry_qualification_image']
        if 'institutional_organization_pic' in d:
            o.institutional_organization_pic = d['institutional_organization_pic']
        if 'legal_person_license_auth_pic' in d:
            o.legal_person_license_auth_pic = d['legal_person_license_auth_pic']
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
        if 'pc_site' in d:
            o.pc_site = d['pc_site']
        if 'pc_site_status' in d:
            o.pc_site_status = d['pc_site_status']
        if 'private_nonenterprise_units' in d:
            o.private_nonenterprise_units = d['private_nonenterprise_units']
        if 'quota_per_day' in d:
            o.quota_per_day = d['quota_per_day']
        if 'quota_per_each' in d:
            o.quota_per_each = d['quota_per_each']
        if 'run_school_license_pic' in d:
            o.run_school_license_pic = d['run_school_license_pic']
        if 'settled_pic' in d:
            o.settled_pic = d['settled_pic']
        if 'shop_entrance_pic' in d:
            o.shop_entrance_pic = d['shop_entrance_pic']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        if 'withhold_service_desc' in d:
            o.withhold_service_desc = d['withhold_service_desc']
        if 'withhold_service_name' in d:
            o.withhold_service_name = d['withhold_service_name']
        return o


