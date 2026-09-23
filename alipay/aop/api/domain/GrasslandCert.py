#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GrasslandCert(object):

    def __init__(self):
        self._apply_time = None
        self._cert_stamp = None
        self._certificate_id = None
        self._display_info = None
        self._donator_image = None
        self._energy = None
        self._organization = None
        self._organization_icon_url = None
        self._plant_place = None
        self._project_id = None
        self._project_name = None
        self._region = None
        self._region_code = None
        self._source = None
        self._template_id = None
        self._tree_name = None
        self._type = None

    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def cert_stamp(self):
        return self._cert_stamp

    @cert_stamp.setter
    def cert_stamp(self, value):
        self._cert_stamp = value
    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def display_info(self):
        return self._display_info

    @display_info.setter
    def display_info(self, value):
        self._display_info = value
    @property
    def donator_image(self):
        return self._donator_image

    @donator_image.setter
    def donator_image(self, value):
        self._donator_image = value
    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        self._energy = value
    @property
    def organization(self):
        return self._organization

    @organization.setter
    def organization(self, value):
        self._organization = value
    @property
    def organization_icon_url(self):
        return self._organization_icon_url

    @organization_icon_url.setter
    def organization_icon_url(self, value):
        self._organization_icon_url = value
    @property
    def plant_place(self):
        return self._plant_place

    @plant_place.setter
    def plant_place(self, value):
        self._plant_place = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def region_code(self):
        return self._region_code

    @region_code.setter
    def region_code(self, value):
        self._region_code = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def tree_name(self):
        return self._tree_name

    @tree_name.setter
    def tree_name(self, value):
        self._tree_name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.cert_stamp:
            if hasattr(self.cert_stamp, 'to_alipay_dict'):
                params['cert_stamp'] = self.cert_stamp.to_alipay_dict()
            else:
                params['cert_stamp'] = self.cert_stamp
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.display_info:
            if hasattr(self.display_info, 'to_alipay_dict'):
                params['display_info'] = self.display_info.to_alipay_dict()
            else:
                params['display_info'] = self.display_info
        if self.donator_image:
            if hasattr(self.donator_image, 'to_alipay_dict'):
                params['donator_image'] = self.donator_image.to_alipay_dict()
            else:
                params['donator_image'] = self.donator_image
        if self.energy:
            if hasattr(self.energy, 'to_alipay_dict'):
                params['energy'] = self.energy.to_alipay_dict()
            else:
                params['energy'] = self.energy
        if self.organization:
            if hasattr(self.organization, 'to_alipay_dict'):
                params['organization'] = self.organization.to_alipay_dict()
            else:
                params['organization'] = self.organization
        if self.organization_icon_url:
            if hasattr(self.organization_icon_url, 'to_alipay_dict'):
                params['organization_icon_url'] = self.organization_icon_url.to_alipay_dict()
            else:
                params['organization_icon_url'] = self.organization_icon_url
        if self.plant_place:
            if hasattr(self.plant_place, 'to_alipay_dict'):
                params['plant_place'] = self.plant_place.to_alipay_dict()
            else:
                params['plant_place'] = self.plant_place
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.region_code:
            if hasattr(self.region_code, 'to_alipay_dict'):
                params['region_code'] = self.region_code.to_alipay_dict()
            else:
                params['region_code'] = self.region_code
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.tree_name:
            if hasattr(self.tree_name, 'to_alipay_dict'):
                params['tree_name'] = self.tree_name.to_alipay_dict()
            else:
                params['tree_name'] = self.tree_name
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GrasslandCert()
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'cert_stamp' in d:
            o.cert_stamp = d['cert_stamp']
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'display_info' in d:
            o.display_info = d['display_info']
        if 'donator_image' in d:
            o.donator_image = d['donator_image']
        if 'energy' in d:
            o.energy = d['energy']
        if 'organization' in d:
            o.organization = d['organization']
        if 'organization_icon_url' in d:
            o.organization_icon_url = d['organization_icon_url']
        if 'plant_place' in d:
            o.plant_place = d['plant_place']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'project_name' in d:
            o.project_name = d['project_name']
        if 'region' in d:
            o.region = d['region']
        if 'region_code' in d:
            o.region_code = d['region_code']
        if 'source' in d:
            o.source = d['source']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'tree_name' in d:
            o.tree_name = d['tree_name']
        if 'type' in d:
            o.type = d['type']
        return o


