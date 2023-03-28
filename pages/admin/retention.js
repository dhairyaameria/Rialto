import React from "react";

// components

import RetentionCard from "components/Cards/RetentionCard.js";

// layout for page

import Admin from "layouts/Admin.js";

export default function Settings() {
  return (
    <>
      <div className="flex flex-wrap">
        <div className="w-full px-4">
          <RetentionCard />
        </div>
      </div>
    </>
  );
}

Settings.layout = Admin;
