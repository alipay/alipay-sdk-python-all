#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantBaseInfoResponse(object):

    def __init__(self):
        self._city = None
        self._corp_address = None
        self._corp_name = None
        self._corp_nature_code = None
        self._corp_type = None
        self._currency_name = None
        self._district = None
        self._district_encode = None
        self._established_date = None
        self._industry_code = None
        self._is_latest = None
        self._issue_date = None
        self._legal_representative = None
        self._legal_representative_id = None
        self._operating_dur = None
        self._operating_scope = None
        self._operating_status = None
        self._org_code = None
        self._province = None
        self._record_authority = None
        self._reg_capital_pub = None
        self._reg_num = None
        self._telephone = None
        self._third_level_industry = None
        self._unified_social_credit_code = None
        self._used_name = None
        self._website = None

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def corp_address(self):
        return self._corp_address

    @corp_address.setter
    def corp_address(self, value):
        self._corp_address = value
    @property
    def corp_name(self):
        return self._corp_name

    @corp_name.setter
    def corp_name(self, value):
        self._corp_name = value
    @property
    def corp_nature_code(self):
        return self._corp_nature_code

    @corp_nature_code.setter
    def corp_nature_code(self, value):
        self._corp_nature_code = value
    @property
    def corp_type(self):
        return self._corp_type

    @corp_type.setter
    def corp_type(self, value):
        self._corp_type = value
    @property
    def currency_name(self):
        return self._currency_name

    @currency_name.setter
    def currency_name(self, value):
        self._currency_name = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def district_encode(self):
        return self._district_encode

    @district_encode.setter
    def district_encode(self, value):
        self._district_encode = value
    @property
    def established_date(self):
        return self._established_date

    @established_date.setter
    def established_date(self, value):
        self._established_date = value
    @property
    def industry_code(self):
        return self._industry_code

    @industry_code.setter
    def industry_code(self, value):
        self._industry_code = value
    @property
    def is_latest(self):
        return self._is_latest

    @is_latest.setter
    def is_latest(self, value):
        self._is_latest = value
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
    @property
    def legal_representative(self):
        return self._legal_representative

    @legal_representative.setter
    def legal_representative(self, value):
        self._legal_representative = value
    @property
    def legal_representative_id(self):
        return self._legal_representative_id

    @legal_representative_id.setter
    def legal_representative_id(self, value):
        self._legal_representative_id = value
    @property
    def operating_dur(self):
        return self._operating_dur

    @operating_dur.setter
    def operating_dur(self, value):
        self._operating_dur = value
    @property
    def operating_scope(self):
        return self._operating_scope

    @operating_scope.setter
    def operating_scope(self, value):
        self._operating_scope = value
    @property
    def operating_status(self):
        return self._operating_status

    @operating_status.setter
    def operating_status(self, value):
        self._operating_status = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def record_authority(self):
        return self._record_authority

    @record_authority.setter
    def record_authority(self, value):
        self._record_authority = value
    @property
    def reg_capital_pub(self):
        return self._reg_capital_pub

    @reg_capital_pub.setter
    def reg_capital_pub(self, value):
        self._reg_capital_pub = value
    @property
    def reg_num(self):
        return self._reg_num

    @reg_num.setter
    def reg_num(self, value):
        self._reg_num = value
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value
    @property
    def third_level_industry(self):
        return self._third_level_industry

    @third_level_industry.setter
    def third_level_industry(self, value):
        self._third_level_industry = value
    @property
    def unified_social_credit_code(self):
        return self._unified_social_credit_code

    @unified_social_credit_code.setter
    def unified_social_credit_code(self, value):
        self._unified_social_credit_code = value
    @property
    def used_name(self):
        return self._used_name

    @used_name.setter
    def used_name(self, value):
        self._used_name = value
    @property
    def website(self):
        return self._website

    @website.setter
    def website(self, value):
        self._website = value


    def to_alipay_dict(self):
        params = dict()
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.corp_address:
            if hasattr(self.corp_address, 'to_alipay_dict'):
                params['corp_address'] = self.corp_address.to_alipay_dict()
            else:
                params['corp_address'] = self.corp_address
        if self.corp_name:
            if hasattr(self.corp_name, 'to_alipay_dict'):
                params['corp_name'] = self.corp_name.to_alipay_dict()
            else:
                params['corp_name'] = self.corp_name
        if self.corp_nature_code:
            if hasattr(self.corp_nature_code, 'to_alipay_dict'):
                params['corp_nature_code'] = self.corp_nature_code.to_alipay_dict()
            else:
                params['corp_nature_code'] = self.corp_nature_code
        if self.corp_type:
            if hasattr(self.corp_type, 'to_alipay_dict'):
                params['corp_type'] = self.corp_type.to_alipay_dict()
            else:
                params['corp_type'] = self.corp_type
        if self.currency_name:
            if hasattr(self.currency_name, 'to_alipay_dict'):
                params['currency_name'] = self.currency_name.to_alipay_dict()
            else:
                params['currency_name'] = self.currency_name
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.district_encode:
            if hasattr(self.district_encode, 'to_alipay_dict'):
                params['district_encode'] = self.district_encode.to_alipay_dict()
            else:
                params['district_encode'] = self.district_encode
        if self.established_date:
            if hasattr(self.established_date, 'to_alipay_dict'):
                params['established_date'] = self.established_date.to_alipay_dict()
            else:
                params['established_date'] = self.established_date
        if self.industry_code:
            if hasattr(self.industry_code, 'to_alipay_dict'):
                params['industry_code'] = self.industry_code.to_alipay_dict()
            else:
                params['industry_code'] = self.industry_code
        if self.is_latest:
            if hasattr(self.is_latest, 'to_alipay_dict'):
                params['is_latest'] = self.is_latest.to_alipay_dict()
            else:
                params['is_latest'] = self.is_latest
        if self.issue_date:
            if hasattr(self.issue_date, 'to_alipay_dict'):
                params['issue_date'] = self.issue_date.to_alipay_dict()
            else:
                params['issue_date'] = self.issue_date
        if self.legal_representative:
            if hasattr(self.legal_representative, 'to_alipay_dict'):
                params['legal_representative'] = self.legal_representative.to_alipay_dict()
            else:
                params['legal_representative'] = self.legal_representative
        if self.legal_representative_id:
            if hasattr(self.legal_representative_id, 'to_alipay_dict'):
                params['legal_representative_id'] = self.legal_representative_id.to_alipay_dict()
            else:
                params['legal_representative_id'] = self.legal_representative_id
        if self.operating_dur:
            if hasattr(self.operating_dur, 'to_alipay_dict'):
                params['operating_dur'] = self.operating_dur.to_alipay_dict()
            else:
                params['operating_dur'] = self.operating_dur
        if self.operating_scope:
            if hasattr(self.operating_scope, 'to_alipay_dict'):
                params['operating_scope'] = self.operating_scope.to_alipay_dict()
            else:
                params['operating_scope'] = self.operating_scope
        if self.operating_status:
            if hasattr(self.operating_status, 'to_alipay_dict'):
                params['operating_status'] = self.operating_status.to_alipay_dict()
            else:
                params['operating_status'] = self.operating_status
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.record_authority:
            if hasattr(self.record_authority, 'to_alipay_dict'):
                params['record_authority'] = self.record_authority.to_alipay_dict()
            else:
                params['record_authority'] = self.record_authority
        if self.reg_capital_pub:
            if hasattr(self.reg_capital_pub, 'to_alipay_dict'):
                params['reg_capital_pub'] = self.reg_capital_pub.to_alipay_dict()
            else:
                params['reg_capital_pub'] = self.reg_capital_pub
        if self.reg_num:
            if hasattr(self.reg_num, 'to_alipay_dict'):
                params['reg_num'] = self.reg_num.to_alipay_dict()
            else:
                params['reg_num'] = self.reg_num
        if self.telephone:
            if hasattr(self.telephone, 'to_alipay_dict'):
                params['telephone'] = self.telephone.to_alipay_dict()
            else:
                params['telephone'] = self.telephone
        if self.third_level_industry:
            if hasattr(self.third_level_industry, 'to_alipay_dict'):
                params['third_level_industry'] = self.third_level_industry.to_alipay_dict()
            else:
                params['third_level_industry'] = self.third_level_industry
        if self.unified_social_credit_code:
            if hasattr(self.unified_social_credit_code, 'to_alipay_dict'):
                params['unified_social_credit_code'] = self.unified_social_credit_code.to_alipay_dict()
            else:
                params['unified_social_credit_code'] = self.unified_social_credit_code
        if self.used_name:
            if hasattr(self.used_name, 'to_alipay_dict'):
                params['used_name'] = self.used_name.to_alipay_dict()
            else:
                params['used_name'] = self.used_name
        if self.website:
            if hasattr(self.website, 'to_alipay_dict'):
                params['website'] = self.website.to_alipay_dict()
            else:
                params['website'] = self.website
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantBaseInfoResponse()
        if 'city' in d:
            o.city = d['city']
        if 'corp_address' in d:
            o.corp_address = d['corp_address']
        if 'corp_name' in d:
            o.corp_name = d['corp_name']
        if 'corp_nature_code' in d:
            o.corp_nature_code = d['corp_nature_code']
        if 'corp_type' in d:
            o.corp_type = d['corp_type']
        if 'currency_name' in d:
            o.currency_name = d['currency_name']
        if 'district' in d:
            o.district = d['district']
        if 'district_encode' in d:
            o.district_encode = d['district_encode']
        if 'established_date' in d:
            o.established_date = d['established_date']
        if 'industry_code' in d:
            o.industry_code = d['industry_code']
        if 'is_latest' in d:
            o.is_latest = d['is_latest']
        if 'issue_date' in d:
            o.issue_date = d['issue_date']
        if 'legal_representative' in d:
            o.legal_representative = d['legal_representative']
        if 'legal_representative_id' in d:
            o.legal_representative_id = d['legal_representative_id']
        if 'operating_dur' in d:
            o.operating_dur = d['operating_dur']
        if 'operating_scope' in d:
            o.operating_scope = d['operating_scope']
        if 'operating_status' in d:
            o.operating_status = d['operating_status']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'province' in d:
            o.province = d['province']
        if 'record_authority' in d:
            o.record_authority = d['record_authority']
        if 'reg_capital_pub' in d:
            o.reg_capital_pub = d['reg_capital_pub']
        if 'reg_num' in d:
            o.reg_num = d['reg_num']
        if 'telephone' in d:
            o.telephone = d['telephone']
        if 'third_level_industry' in d:
            o.third_level_industry = d['third_level_industry']
        if 'unified_social_credit_code' in d:
            o.unified_social_credit_code = d['unified_social_credit_code']
        if 'used_name' in d:
            o.used_name = d['used_name']
        if 'website' in d:
            o.website = d['website']
        return o


