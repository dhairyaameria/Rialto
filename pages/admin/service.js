import React from "react";

// components

import ServiceCard from "components/Cards/ServiceCard.js";

// layout for page

import Admin from "layouts/Admin.js";

export default function Settings() {
  return (
    <>
      <div className="flex flex-wrap">
        <div className="w-full px-4">
          <ServiceCard />
        </div>
      </div>
    </>
  );
}

Settings.layout = Admin;
