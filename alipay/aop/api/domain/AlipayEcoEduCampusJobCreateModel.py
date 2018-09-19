#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoEduCampusJobCreateModel(object):

    def __init__(self):
        self._area_city_code = None
        self._area_city_name = None
        self._area_district_code = None
        self._area_district_name = None
        self._area_job_address = None
        self._area_province_code = None
        self._area_province_name = None
        self._area_street_name = None
        self._company_lawname = None
        self._company_logo = None
        self._company_name = None
        self._company_source = None
        self._content_var = None
        self._gmt_expired = None
        self._gmt_refresh = None
        self._gmt_start = None
        self._job_desc = None
        self._job_hire_number = None
        self._job_name = None
        self._job_perk = None
        self._job_resume_lg = None
        self._job_rq_education = None
        self._job_tier_one_code = None
        self._job_tier_one_name = None
        self._job_tier_three_code = None
        self._job_tier_three_name = None
        self._job_tier_two_code = None
        self._job_tier_two_name = None
        self._job_type = None
        self._payment_max = None
        self._payment_min = None
        self._payment_unit = None
        self._source_code = None
        self._source_id = None
        self._tra_job_freq = None
        self._tra_job_period = None
        self._tra_job_promot = None

    @property
    def area_city_code(self):
        return self._area_city_code

    @area_city_code.setter
    def area_city_code(self, value):
        self._area_city_code = value
    @property
    def area_city_name(self):
        return self._area_city_name

    @area_city_name.setter
    def area_city_name(self, value):
        self._area_city_name = value
    @property
    def area_district_code(self):
        return self._area_district_code

    @area_district_code.setter
    def area_district_code(self, value):
        self._area_district_code = value
    @property
    def area_district_name(self):
        return self._area_district_name

    @area_district_name.setter
    def area_district_name(self, value):
        self._area_district_name = value
    @property
    def area_job_address(self):
        return self._area_job_address

    @area_job_address.setter
    def area_job_address(self, value):
        self._area_job_address = value
    @property
    def area_province_code(self):
        return self._area_province_code

    @area_province_code.setter
    def area_province_code(self, value):
        self._area_province_code = value
    @property
    def area_province_name(self):
        return self._area_province_name

    @area_province_name.setter
    def area_province_name(self, value):
        self._area_province_name = value
    @property
    def area_street_name(self):
        return self._area_street_name

    @area_street_name.setter
    def area_street_name(self, value):
        self._area_street_name = value
    @property
    def company_lawname(self):
        return self._company_lawname

    @company_lawname.setter
    def company_lawname(self, value):
        self._company_lawname = value
    @property
    def company_logo(self):
        return self._company_logo

    @company_logo.setter
    def company_logo(self, value):
        self._company_logo = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def company_source(self):
        return self._company_source

    @company_source.setter
    def company_source(self, value):
        self._company_source = value
    @property
    def content_var(self):
        return self._content_var

    @content_var.setter
    def content_var(self, value):
        self._content_var = value
    @property
    def gmt_expired(self):
        return self._gmt_expired

    @gmt_expired.setter
    def gmt_expired(self, value):
        self._gmt_expired = value
    @property
    def gmt_refresh(self):
        return self._gmt_refresh

    @gmt_refresh.setter
    def gmt_refresh(self, value):
        self._gmt_refresh = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def job_desc(self):
        return self._job_desc

    @job_desc.setter
    def job_desc(self, value):
        self._job_desc = value
    @property
    def job_hire_number(self):
        return self._job_hire_number

    @job_hire_number.setter
    def job_hire_number(self, value):
        self._job_hire_number = value
    @property
    def job_name(self):
        return self._job_name

    @job_name.setter
    def job_name(self, value):
        self._job_name = value
    @property
    def job_perk(self):
        return self._job_perk

    @job_perk.setter
    def job_perk(self, value):
        self._job_perk = value
    @property
    def job_resume_lg(self):
        return self._job_resume_lg

    @job_resume_lg.setter
    def job_resume_lg(self, value):
        self._job_resume_lg = value
    @property
    def job_rq_education(self):
        return self._job_rq_education

    @job_rq_education.setter
    def job_rq_education(self, value):
        self._job_rq_education = value
    @property
    def job_tier_one_code(self):
        return self._job_tier_one_code

    @job_tier_one_code.setter
    def job_tier_one_code(self, value):
        self._job_tier_one_code = value
    @property
    def job_tier_one_name(self):
        return self._job_tier_one_name

    @job_tier_one_name.setter
    def job_tier_one_name(self, value):
        self._job_tier_one_name = value
    @property
    def job_tier_three_code(self):
        return self._job_tier_three_code

    @job_tier_three_code.setter
    def job_tier_three_code(self, value):
        self._job_tier_three_code = value
    @property
    def job_tier_three_name(self):
        return self._job_tier_three_name

    @job_tier_three_name.setter
    def job_tier_three_name(self, value):
        self._job_tier_three_name = value
    @property
    def job_tier_two_code(self):
        return self._job_tier_two_code

    @job_tier_two_code.setter
    def job_tier_two_code(self, value):
        self._job_tier_two_code = value
    @property
    def job_tier_two_name(self):
        return self._job_tier_two_name

    @job_tier_two_name.setter
    def job_tier_two_name(self, value):
        self._job_tier_two_name = value
    @property
    def job_type(self):
        return self._job_type

    @job_type.setter
    def job_type(self, value):
        self._job_type = value
    @property
    def payment_max(self):
        return self._payment_max

    @payment_max.setter
    def payment_max(self, value):
        self._payment_max = value
    @property
    def payment_min(self):
        return self._payment_min

    @payment_min.setter
    def payment_min(self, value):
        self._payment_min = value
    @property
    def payment_unit(self):
        return self._payment_unit

    @payment_unit.setter
    def payment_unit(self, value):
        self._payment_unit = value
    @property
    def source_code(self):
        return self._source_code

    @source_code.setter
    def source_code(self, value):
        self._source_code = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def tra_job_freq(self):
        return self._tra_job_freq

    @tra_job_freq.setter
    def tra_job_freq(self, value):
        self._tra_job_freq = value
    @property
    def tra_job_period(self):
        return self._tra_job_period

    @tra_job_period.setter
    def tra_job_period(self, value):
        self._tra_job_period = value
    @property
    def tra_job_promot(self):
        return self._tra_job_promot

    @tra_job_promot.setter
    def tra_job_promot(self, value):
        self._tra_job_promot = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_city_code:
            if hasattr(self.area_city_code, 'to_alipay_dict'):
                params['area_city_code'] = self.area_city_code.to_alipay_dict()
            else:
                params['area_city_code'] = self.area_city_code
        if self.area_city_name:
            if hasattr(self.area_city_name, 'to_alipay_dict'):
                params['area_city_name'] = self.area_city_name.to_alipay_dict()
            else:
                params['area_city_name'] = self.area_city_name
        if self.area_district_code:
            if hasattr(self.area_district_code, 'to_alipay_dict'):
                params['area_district_code'] = self.area_district_code.to_alipay_dict()
            else:
                params['area_district_code'] = self.area_district_code
        if self.area_district_name:
            if hasattr(self.area_district_name, 'to_alipay_dict'):
                params['area_district_name'] = self.area_district_name.to_alipay_dict()
            else:
                params['area_district_name'] = self.area_district_name
        if self.area_job_address:
            if hasattr(self.area_job_address, 'to_alipay_dict'):
                params['area_job_address'] = self.area_job_address.to_alipay_dict()
            else:
                params['area_job_address'] = self.area_job_address
        if self.area_province_code:
            if hasattr(self.area_province_code, 'to_alipay_dict'):
                params['area_province_code'] = self.area_province_code.to_alipay_dict()
            else:
                params['area_province_code'] = self.area_province_code
        if self.area_province_name:
            if hasattr(self.area_province_name, 'to_alipay_dict'):
                params['area_province_name'] = self.area_province_name.to_alipay_dict()
            else:
                params['area_province_name'] = self.area_province_name
        if self.area_street_name:
            if hasattr(self.area_street_name, 'to_alipay_dict'):
                params['area_street_name'] = self.area_street_name.to_alipay_dict()
            else:
                params['area_street_name'] = self.area_street_name
        if self.company_lawname:
            if hasattr(self.company_lawname, 'to_alipay_dict'):
                params['company_lawname'] = self.company_lawname.to_alipay_dict()
            else:
                params['company_lawname'] = self.company_lawname
        if self.company_logo:
            if hasattr(self.company_logo, 'to_alipay_dict'):
                params['company_logo'] = self.company_logo.to_alipay_dict()
            else:
                params['company_logo'] = self.company_logo
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.company_source:
            if hasattr(self.company_source, 'to_alipay_dict'):
                params['company_source'] = self.company_source.to_alipay_dict()
            else:
                params['company_source'] = self.company_source
        if self.content_var:
            if hasattr(self.content_var, 'to_alipay_dict'):
                params['content_var'] = self.content_var.to_alipay_dict()
            else:
                params['content_var'] = self.content_var
        if self.gmt_expired:
            if hasattr(self.gmt_expired, 'to_alipay_dict'):
                params['gmt_expired'] = self.gmt_expired.to_alipay_dict()
            else:
                params['gmt_expired'] = self.gmt_expired
        if self.gmt_refresh:
            if hasattr(self.gmt_refresh, 'to_alipay_dict'):
                params['gmt_refresh'] = self.gmt_refresh.to_alipay_dict()
            else:
                params['gmt_refresh'] = self.gmt_refresh
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.job_desc:
            if hasattr(self.job_desc, 'to_alipay_dict'):
                params['job_desc'] = self.job_desc.to_alipay_dict()
            else:
                params['job_desc'] = self.job_desc
        if self.job_hire_number:
            if hasattr(self.job_hire_number, 'to_alipay_dict'):
                params['job_hire_number'] = self.job_hire_number.to_alipay_dict()
            else:
                params['job_hire_number'] = self.job_hire_number
        if self.job_name:
            if hasattr(self.job_name, 'to_alipay_dict'):
                params['job_name'] = self.job_name.to_alipay_dict()
            else:
                params['job_name'] = self.job_name
        if self.job_perk:
            if hasattr(self.job_perk, 'to_alipay_dict'):
                params['job_perk'] = self.job_perk.to_alipay_dict()
            else:
                params['job_perk'] = self.job_perk
        if self.job_resume_lg:
            if hasattr(self.job_resume_lg, 'to_alipay_dict'):
                params['job_resume_lg'] = self.job_resume_lg.to_alipay_dict()
            else:
                params['job_resume_lg'] = self.job_resume_lg
        if self.job_rq_education:
            if hasattr(self.job_rq_education, 'to_alipay_dict'):
                params['job_rq_education'] = self.job_rq_education.to_alipay_dict()
            else:
                params['job_rq_education'] = self.job_rq_education
        if self.job_tier_one_code:
            if hasattr(self.job_tier_one_code, 'to_alipay_dict'):
                params['job_tier_one_code'] = self.job_tier_one_code.to_alipay_dict()
            else:
                params['job_tier_one_code'] = self.job_tier_one_code
        if self.job_tier_one_name:
            if hasattr(self.job_tier_one_name, 'to_alipay_dict'):
                params['job_tier_one_name'] = self.job_tier_one_name.to_alipay_dict()
            else:
                params['job_tier_one_name'] = self.job_tier_one_name
        if self.job_tier_three_code:
            if hasattr(self.job_tier_three_code, 'to_alipay_dict'):
                params['job_tier_three_code'] = self.job_tier_three_code.to_alipay_dict()
            else:
                params['job_tier_three_code'] = self.job_tier_three_code
        if self.job_tier_three_name:
            if hasattr(self.job_tier_three_name, 'to_alipay_dict'):
                params['job_tier_three_name'] = self.job_tier_three_name.to_alipay_dict()
            else:
                params['job_tier_three_name'] = self.job_tier_three_name
        if self.job_tier_two_code:
            if hasattr(self.job_tier_two_code, 'to_alipay_dict'):
                params['job_tier_two_code'] = self.job_tier_two_code.to_alipay_dict()
            else:
                params['job_tier_two_code'] = self.job_tier_two_code
        if self.job_tier_two_name:
            if hasattr(self.job_tier_two_name, 'to_alipay_dict'):
                params['job_tier_two_name'] = self.job_tier_two_name.to_alipay_dict()
            else:
                params['job_tier_two_name'] = self.job_tier_two_name
        if self.job_type:
            if hasattr(self.job_type, 'to_alipay_dict'):
                params['job_type'] = self.job_type.to_alipay_dict()
            else:
                params['job_type'] = self.job_type
        if self.payment_max:
            if hasattr(self.payment_max, 'to_alipay_dict'):
                params['payment_max'] = self.payment_max.to_alipay_dict()
            else:
                params['payment_max'] = self.payment_max
        if self.payment_min:
            if hasattr(self.payment_min, 'to_alipay_dict'):
                params['payment_min'] = self.payment_min.to_alipay_dict()
            else:
                params['payment_min'] = self.payment_min
        if self.payment_unit:
            if hasattr(self.payment_unit, 'to_alipay_dict'):
                params['payment_unit'] = self.payment_unit.to_alipay_dict()
            else:
                params['payment_unit'] = self.payment_unit
        if self.source_code:
            if hasattr(self.source_code, 'to_alipay_dict'):
                params['source_code'] = self.source_code.to_alipay_dict()
            else:
                params['source_code'] = self.source_code
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.tra_job_freq:
            if hasattr(self.tra_job_freq, 'to_alipay_dict'):
                params['tra_job_freq'] = self.tra_job_freq.to_alipay_dict()
            else:
                params['tra_job_freq'] = self.tra_job_freq
        if self.tra_job_period:
            if hasattr(self.tra_job_period, 'to_alipay_dict'):
                params['tra_job_period'] = self.tra_job_period.to_alipay_dict()
            else:
                params['tra_job_period'] = self.tra_job_period
        if self.tra_job_promot:
            if hasattr(self.tra_job_promot, 'to_alipay_dict'):
                params['tra_job_promot'] = self.tra_job_promot.to_alipay_dict()
            else:
                params['tra_job_promot'] = self.tra_job_promot
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEduCampusJobCreateModel()
        if 'area_city_code' in d:
            o.area_city_code = d['area_city_code']
        if 'area_city_name' in d:
            o.area_city_name = d['area_city_name']
        if 'area_district_code' in d:
            o.area_district_code = d['area_district_code']
        if 'area_district_name' in d:
            o.area_district_name = d['area_district_name']
        if 'area_job_address' in d:
            o.area_job_address = d['area_job_address']
        if 'area_province_code' in d:
            o.area_province_code = d['area_province_code']
        if 'area_province_name' in d:
            o.area_province_name = d['area_province_name']
        if 'area_street_name' in d:
            o.area_street_name = d['area_street_name']
        if 'company_lawname' in d:
            o.company_lawname = d['company_lawname']
        if 'company_logo' in d:
            o.company_logo = d['company_logo']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'company_source' in d:
            o.company_source = d['company_source']
        if 'content_var' in d:
            o.content_var = d['content_var']
        if 'gmt_expired' in d:
            o.gmt_expired = d['gmt_expired']
        if 'gmt_refresh' in d:
            o.gmt_refresh = d['gmt_refresh']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'job_desc' in d:
            o.job_desc = d['job_desc']
        if 'job_hire_number' in d:
            o.job_hire_number = d['job_hire_number']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'job_perk' in d:
            o.job_perk = d['job_perk']
        if 'job_resume_lg' in d:
            o.job_resume_lg = d['job_resume_lg']
        if 'job_rq_education' in d:
            o.job_rq_education = d['job_rq_education']
        if 'job_tier_one_code' in d:
            o.job_tier_one_code = d['job_tier_one_code']
        if 'job_tier_one_name' in d:
            o.job_tier_one_name = d['job_tier_one_name']
        if 'job_tier_three_code' in d:
            o.job_tier_three_code = d['job_tier_three_code']
        if 'job_tier_three_name' in d:
            o.job_tier_three_name = d['job_tier_three_name']
        if 'job_tier_two_code' in d:
            o.job_tier_two_code = d['job_tier_two_code']
        if 'job_tier_two_name' in d:
            o.job_tier_two_name = d['job_tier_two_name']
        if 'job_type' in d:
            o.job_type = d['job_type']
        if 'payment_max' in d:
            o.payment_max = d['payment_max']
        if 'payment_min' in d:
            o.payment_min = d['payment_min']
        if 'payment_unit' in d:
            o.payment_unit = d['payment_unit']
        if 'source_code' in d:
            o.source_code = d['source_code']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'tra_job_freq' in d:
            o.tra_job_freq = d['tra_job_freq']
        if 'tra_job_period' in d:
            o.tra_job_period = d['tra_job_period']
        if 'tra_job_promot' in d:
            o.tra_job_promot = d['tra_job_promot']
        return o


