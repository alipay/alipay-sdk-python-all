#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoEduCampusJobtalkCreateModel(object):

    def __init__(self):
        self._campany_source = None
        self._city = None
        self._city_code = None
        self._company_lawname = None
        self._company_name = None
        self._content_var = None
        self._district = None
        self._latitude = None
        self._logo_url = None
        self._longitude = None
        self._province = None
        self._province_code = None
        self._street = None
        self._talk_address = None
        self._talk_content = None
        self._talk_endtime = None
        self._talk_holdtime = None
        self._talk_school_code = None
        self._talk_school_name = None
        self._talk_source_code = None
        self._talk_source_id = None
        self._talk_title = None
        self._talk_type = None
        self._talksource_source = None
        self._web_url = None

    @property
    def campany_source(self):
        return self._campany_source

    @campany_source.setter
    def campany_source(self, value):
        self._campany_source = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def company_lawname(self):
        return self._company_lawname

    @company_lawname.setter
    def company_lawname(self, value):
        self._company_lawname = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def content_var(self):
        return self._content_var

    @content_var.setter
    def content_var(self, value):
        self._content_var = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        self._street = value
    @property
    def talk_address(self):
        return self._talk_address

    @talk_address.setter
    def talk_address(self, value):
        self._talk_address = value
    @property
    def talk_content(self):
        return self._talk_content

    @talk_content.setter
    def talk_content(self, value):
        self._talk_content = value
    @property
    def talk_endtime(self):
        return self._talk_endtime

    @talk_endtime.setter
    def talk_endtime(self, value):
        self._talk_endtime = value
    @property
    def talk_holdtime(self):
        return self._talk_holdtime

    @talk_holdtime.setter
    def talk_holdtime(self, value):
        self._talk_holdtime = value
    @property
    def talk_school_code(self):
        return self._talk_school_code

    @talk_school_code.setter
    def talk_school_code(self, value):
        self._talk_school_code = value
    @property
    def talk_school_name(self):
        return self._talk_school_name

    @talk_school_name.setter
    def talk_school_name(self, value):
        self._talk_school_name = value
    @property
    def talk_source_code(self):
        return self._talk_source_code

    @talk_source_code.setter
    def talk_source_code(self, value):
        self._talk_source_code = value
    @property
    def talk_source_id(self):
        return self._talk_source_id

    @talk_source_id.setter
    def talk_source_id(self, value):
        self._talk_source_id = value
    @property
    def talk_title(self):
        return self._talk_title

    @talk_title.setter
    def talk_title(self, value):
        self._talk_title = value
    @property
    def talk_type(self):
        return self._talk_type

    @talk_type.setter
    def talk_type(self, value):
        self._talk_type = value
    @property
    def talksource_source(self):
        return self._talksource_source

    @talksource_source.setter
    def talksource_source(self, value):
        self._talksource_source = value
    @property
    def web_url(self):
        return self._web_url

    @web_url.setter
    def web_url(self, value):
        self._web_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.campany_source:
            if hasattr(self.campany_source, 'to_alipay_dict'):
                params['campany_source'] = self.campany_source.to_alipay_dict()
            else:
                params['campany_source'] = self.campany_source
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.company_lawname:
            if hasattr(self.company_lawname, 'to_alipay_dict'):
                params['company_lawname'] = self.company_lawname.to_alipay_dict()
            else:
                params['company_lawname'] = self.company_lawname
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.content_var:
            if hasattr(self.content_var, 'to_alipay_dict'):
                params['content_var'] = self.content_var.to_alipay_dict()
            else:
                params['content_var'] = self.content_var
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.street:
            if hasattr(self.street, 'to_alipay_dict'):
                params['street'] = self.street.to_alipay_dict()
            else:
                params['street'] = self.street
        if self.talk_address:
            if hasattr(self.talk_address, 'to_alipay_dict'):
                params['talk_address'] = self.talk_address.to_alipay_dict()
            else:
                params['talk_address'] = self.talk_address
        if self.talk_content:
            if hasattr(self.talk_content, 'to_alipay_dict'):
                params['talk_content'] = self.talk_content.to_alipay_dict()
            else:
                params['talk_content'] = self.talk_content
        if self.talk_endtime:
            if hasattr(self.talk_endtime, 'to_alipay_dict'):
                params['talk_endtime'] = self.talk_endtime.to_alipay_dict()
            else:
                params['talk_endtime'] = self.talk_endtime
        if self.talk_holdtime:
            if hasattr(self.talk_holdtime, 'to_alipay_dict'):
                params['talk_holdtime'] = self.talk_holdtime.to_alipay_dict()
            else:
                params['talk_holdtime'] = self.talk_holdtime
        if self.talk_school_code:
            if hasattr(self.talk_school_code, 'to_alipay_dict'):
                params['talk_school_code'] = self.talk_school_code.to_alipay_dict()
            else:
                params['talk_school_code'] = self.talk_school_code
        if self.talk_school_name:
            if hasattr(self.talk_school_name, 'to_alipay_dict'):
                params['talk_school_name'] = self.talk_school_name.to_alipay_dict()
            else:
                params['talk_school_name'] = self.talk_school_name
        if self.talk_source_code:
            if hasattr(self.talk_source_code, 'to_alipay_dict'):
                params['talk_source_code'] = self.talk_source_code.to_alipay_dict()
            else:
                params['talk_source_code'] = self.talk_source_code
        if self.talk_source_id:
            if hasattr(self.talk_source_id, 'to_alipay_dict'):
                params['talk_source_id'] = self.talk_source_id.to_alipay_dict()
            else:
                params['talk_source_id'] = self.talk_source_id
        if self.talk_title:
            if hasattr(self.talk_title, 'to_alipay_dict'):
                params['talk_title'] = self.talk_title.to_alipay_dict()
            else:
                params['talk_title'] = self.talk_title
        if self.talk_type:
            if hasattr(self.talk_type, 'to_alipay_dict'):
                params['talk_type'] = self.talk_type.to_alipay_dict()
            else:
                params['talk_type'] = self.talk_type
        if self.talksource_source:
            if hasattr(self.talksource_source, 'to_alipay_dict'):
                params['talksource_source'] = self.talksource_source.to_alipay_dict()
            else:
                params['talksource_source'] = self.talksource_source
        if self.web_url:
            if hasattr(self.web_url, 'to_alipay_dict'):
                params['web_url'] = self.web_url.to_alipay_dict()
            else:
                params['web_url'] = self.web_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEduCampusJobtalkCreateModel()
        if 'campany_source' in d:
            o.campany_source = d['campany_source']
        if 'city' in d:
            o.city = d['city']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'company_lawname' in d:
            o.company_lawname = d['company_lawname']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'content_var' in d:
            o.content_var = d['content_var']
        if 'district' in d:
            o.district = d['district']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'province' in d:
            o.province = d['province']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'street' in d:
            o.street = d['street']
        if 'talk_address' in d:
            o.talk_address = d['talk_address']
        if 'talk_content' in d:
            o.talk_content = d['talk_content']
        if 'talk_endtime' in d:
            o.talk_endtime = d['talk_endtime']
        if 'talk_holdtime' in d:
            o.talk_holdtime = d['talk_holdtime']
        if 'talk_school_code' in d:
            o.talk_school_code = d['talk_school_code']
        if 'talk_school_name' in d:
            o.talk_school_name = d['talk_school_name']
        if 'talk_source_code' in d:
            o.talk_source_code = d['talk_source_code']
        if 'talk_source_id' in d:
            o.talk_source_id = d['talk_source_id']
        if 'talk_title' in d:
            o.talk_title = d['talk_title']
        if 'talk_type' in d:
            o.talk_type = d['talk_type']
        if 'talksource_source' in d:
            o.talksource_source = d['talksource_source']
        if 'web_url' in d:
            o.web_url = d['web_url']
        return o


