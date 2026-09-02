#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RouteInfoObject(object):

    def __init__(self):
        self._connected_metro_route_information = None
        self._operational_statistics = None
        self._optimization_recommendations = None
        self._route_basic_information = None
        self._route_comprehensive_assessment = None
        self._route_diagnosis = None
        self._route_name = None
        self._route_score = None

    @property
    def connected_metro_route_information(self):
        return self._connected_metro_route_information

    @connected_metro_route_information.setter
    def connected_metro_route_information(self, value):
        self._connected_metro_route_information = value
    @property
    def operational_statistics(self):
        return self._operational_statistics

    @operational_statistics.setter
    def operational_statistics(self, value):
        self._operational_statistics = value
    @property
    def optimization_recommendations(self):
        return self._optimization_recommendations

    @optimization_recommendations.setter
    def optimization_recommendations(self, value):
        self._optimization_recommendations = value
    @property
    def route_basic_information(self):
        return self._route_basic_information

    @route_basic_information.setter
    def route_basic_information(self, value):
        self._route_basic_information = value
    @property
    def route_comprehensive_assessment(self):
        return self._route_comprehensive_assessment

    @route_comprehensive_assessment.setter
    def route_comprehensive_assessment(self, value):
        self._route_comprehensive_assessment = value
    @property
    def route_diagnosis(self):
        return self._route_diagnosis

    @route_diagnosis.setter
    def route_diagnosis(self, value):
        self._route_diagnosis = value
    @property
    def route_name(self):
        return self._route_name

    @route_name.setter
    def route_name(self, value):
        self._route_name = value
    @property
    def route_score(self):
        return self._route_score

    @route_score.setter
    def route_score(self, value):
        self._route_score = value


    def to_alipay_dict(self):
        params = dict()
        if self.connected_metro_route_information:
            if hasattr(self.connected_metro_route_information, 'to_alipay_dict'):
                params['connected_metro_route_information'] = self.connected_metro_route_information.to_alipay_dict()
            else:
                params['connected_metro_route_information'] = self.connected_metro_route_information
        if self.operational_statistics:
            if hasattr(self.operational_statistics, 'to_alipay_dict'):
                params['operational_statistics'] = self.operational_statistics.to_alipay_dict()
            else:
                params['operational_statistics'] = self.operational_statistics
        if self.optimization_recommendations:
            if hasattr(self.optimization_recommendations, 'to_alipay_dict'):
                params['optimization_recommendations'] = self.optimization_recommendations.to_alipay_dict()
            else:
                params['optimization_recommendations'] = self.optimization_recommendations
        if self.route_basic_information:
            if hasattr(self.route_basic_information, 'to_alipay_dict'):
                params['route_basic_information'] = self.route_basic_information.to_alipay_dict()
            else:
                params['route_basic_information'] = self.route_basic_information
        if self.route_comprehensive_assessment:
            if hasattr(self.route_comprehensive_assessment, 'to_alipay_dict'):
                params['route_comprehensive_assessment'] = self.route_comprehensive_assessment.to_alipay_dict()
            else:
                params['route_comprehensive_assessment'] = self.route_comprehensive_assessment
        if self.route_diagnosis:
            if hasattr(self.route_diagnosis, 'to_alipay_dict'):
                params['route_diagnosis'] = self.route_diagnosis.to_alipay_dict()
            else:
                params['route_diagnosis'] = self.route_diagnosis
        if self.route_name:
            if hasattr(self.route_name, 'to_alipay_dict'):
                params['route_name'] = self.route_name.to_alipay_dict()
            else:
                params['route_name'] = self.route_name
        if self.route_score:
            if hasattr(self.route_score, 'to_alipay_dict'):
                params['route_score'] = self.route_score.to_alipay_dict()
            else:
                params['route_score'] = self.route_score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RouteInfoObject()
        if 'connected_metro_route_information' in d:
            o.connected_metro_route_information = d['connected_metro_route_information']
        if 'operational_statistics' in d:
            o.operational_statistics = d['operational_statistics']
        if 'optimization_recommendations' in d:
            o.optimization_recommendations = d['optimization_recommendations']
        if 'route_basic_information' in d:
            o.route_basic_information = d['route_basic_information']
        if 'route_comprehensive_assessment' in d:
            o.route_comprehensive_assessment = d['route_comprehensive_assessment']
        if 'route_diagnosis' in d:
            o.route_diagnosis = d['route_diagnosis']
        if 'route_name' in d:
            o.route_name = d['route_name']
        if 'route_score' in d:
            o.route_score = d['route_score']
        return o


